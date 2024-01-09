using Microsoft.Data.SqlClient;
using System.Data;

namespace Lab4DeadlockSgbd
{
    public class Thread1
    {
        string connectionString =
            "Data Source=LAPTOP-MF0S35KN\\SQLEXPRESS;Initial Catalog=Biblioteca;Integrated Security=True;TrustServerCertificate=True";

        int tries = 5;

        public virtual void run()
        {
            Thread.Sleep(1000);
            while (tries > 0)
            {
                Console.WriteLine("Thread 1 is on try: " + tries);
                Console.WriteLine();

                SqlTransaction objTrans = null;

                using (SqlConnection objConn = new SqlConnection(connectionString))
                {
                    objConn.Open();
                    objTrans = objConn.BeginTransaction();
                    try
                    {
                        tries--;
                        SqlCommand objCmd1 = new SqlCommand("update Carti set Titlu='deadlock1' where Cid=5032",
                            objConn, objTrans);
                        SqlCommand objCmd2 = new SqlCommand("waitfor delay '00:00:10'", objConn, objTrans);
                        SqlCommand objCmd3 = new SqlCommand("update Autori set Nume='deadlock1' where Auid=5028",
                            objConn, objTrans);
                        objCmd1.ExecuteNonQuery();
                        objCmd2.ExecuteNonQuery();
                        objCmd3.ExecuteNonQuery();
                        objTrans.Commit();
                    }
                    catch (Exception e)
                    {
                        objTrans.Rollback();
                        Console.WriteLine("Thread 1 " + e.ToString());
                        Console.WriteLine();
                    }
                }
            }

            if (tries == 0)
            {
                Console.WriteLine("Thread 1 " + "S-au efectuat toate incercarile posibile!");
                Console.WriteLine();
            }
        }

        public class Thread2
        {
            string connectionString =
                "Data Source=LAPTOP-MF0S35KN\\SQLEXPRESS;Initial Catalog=Biblioteca;Integrated Security=True;TrustServerCertificate=True";

            SqlDataAdapter daCarti = new SqlDataAdapter();
            private SqlDataAdapter daAutori = new SqlDataAdapter();

            DataSet ds = new DataSet();

            int tries = 5;

            public virtual void run()
            {
                while (tries > 0)
                {
                    Console.WriteLine("Thread 2 is on try: " + tries);
                    Console.WriteLine();
                    SqlTransaction objTrans = null;

                    using (SqlConnection objConn = new SqlConnection(connectionString))
                    {
                        objConn.Open();
                        objTrans = objConn.BeginTransaction();
                        try
                        {
                            tries--;
                            SqlCommand objCmd1 = new SqlCommand("update Autori set Nume='deadlock1' where Auid=5028",
                                objConn, objTrans);
                            SqlCommand objCmd2 = new SqlCommand("waitfor delay '00:00:05'", objConn, objTrans);
                            SqlCommand objCmd3 = new SqlCommand("update Carti set Titlu='deadlock1' where Cid=5032",
                                objConn, objTrans);
                            objCmd1.ExecuteNonQuery();
                            objCmd2.ExecuteNonQuery();
                            objCmd3.ExecuteNonQuery();
                            objTrans.Commit();
                        }
                        catch (Exception e)
                        {
                            objTrans.Rollback();
                            Console.WriteLine("Thread 2 " + e.ToString());
                            Console.WriteLine();
                        }
                    }
                }

                if (tries == 0)
                {
                    Console.WriteLine("Thread 2 " + "S-au efectuat toate incercarile posibile!");
                    Console.WriteLine();
                }
            }
        }

        internal class Program
        {
            static void Main(string[] args)
            {
                Console.WriteLine("Starting deadlock application!");
                Thread1 t1 = new Thread1();
                Thread2 t2 = new Thread2();

                var th1 = new Thread(new ThreadStart(t1.run));
                var th2 = new Thread(new ThreadStart(t2.run));
                th2.Start();
                th1.Start();
            }
        }
    }
}