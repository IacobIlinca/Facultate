using Microsoft.Data.SqlClient;
using System.Data;
namespace Lab1SGBD_V2
{
    public partial class Form1 : Form
    {
        string connectionString = "Data Source=LAPTOP-MF0S35KN\\SQLEXPRESS;Initial Catalog=Biblioteca;Integrated Security=True;TrustServerCertificate=True";
        //SqlConnection connection = new SqlConnection("Data Source=LAPTOP-MF0S35KN\\SQLEXPRESS;Initial Catalog=Biblioteca;Integrated Security=True;TrustServerCertificate=True");
        DataSet ds = new DataSet();
        //SqlDataAdapter parentAdapter = new SqlDataAdapter();
        //SqlDataAdapter childAdapter = new SqlDataAdapter();
        SqlDataAdapter adapter = new SqlDataAdapter();
        //BindingSource parentBS = new BindingSource();
        //BindingSource childBS = new BindingSource();
        int parentId = -1;
        int childId = -1;


        public Form1()
        {
            InitializeComponent();
        }

        public void getParentList()
        {
            try
            {
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    adapter.SelectCommand = new SqlCommand("Select * FROM Adrese_Persoane", connection);
                    adapter.Fill(ds, "Adrese_Persoane");
                    parentId = -1;
                    dataGridViewParent.DataSource = ds.Tables["Adrese_Persoane"];
                    connection.Close();
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        public void getChildList()
        {
            try
            {
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    adapter.SelectCommand = new SqlCommand("Select * FROM Persoane", connection);
                    adapter.Fill(ds, "Persoane");
                    childId = -1;
                    dataGridViewChild.DataSource = ds.Tables["Persoane"];
                    connection.Close();
                }
            }
            catch (Exception e)
            {
                MessageBox.Show(e.Message);
            }
        }

        private void dataGridViewParent_SelectionChanged(object sender, EventArgs e)
        {
            parentId = -1;
            childId = -1;
            DataGridView gridView = sender as DataGridView;
            if (gridView != null && gridView.SelectedRows.Count > 0)
            {
                DataGridViewRow selected = gridView.SelectedRows[0];
                parentId = (int)selected.Cells[0].Value;

                if (selected != null)
                {
                    try
                    {
                        using (SqlConnection connection = new SqlConnection(connectionString))
                        {
                            connection.Open();
                            adapter.SelectCommand = new SqlCommand("Select * FROM Persoane where Aid=@idSelectat;", connection);
                            adapter.SelectCommand.Parameters.AddWithValue("@idSelectat", selected.Cells[0].Value);
                            if (ds.Tables["Persoane"] is not null)
                            {
                                ds.Tables["Persoane"].Clear();
                            }
                            adapter.Fill(ds, "Persoane");
                            childId = -1;
                            dataGridViewChild.DataSource = ds.Tables["Persoane"];
                            connection.Close();
                        }
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show(ex.Message);
                    }
                }
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        private void Form1_Load(object sender, EventArgs e)
        {
            getParentList();
            //getChildList();
        }

        private void buttonDel_Click(object sender, EventArgs e)
        {
            
                    //childId = int.Parse(dataGridViewChild.SelectedRows[0].Cells[0].Value.ToString());

            if (childId != -1)
                    {
                        try
                        {
                            using (SqlConnection connection = new SqlConnection(connectionString))
                            {
                                connection.Open();
                                adapter.DeleteCommand = new SqlCommand("DELETE FROM Persoane WHERE Pid=@pid;", connection);
                                adapter.DeleteCommand.Parameters.AddWithValue("@pid", childId);
                                adapter.DeleteCommand.ExecuteNonQuery();

                                adapter.SelectCommand = new SqlCommand("SELECT * FROM Persoane WHERE Aid=@aid;", connection);
                                adapter.SelectCommand.Parameters.AddWithValue("@aid", parentId);
                                ds.Tables["Persoane"].Clear();
                                adapter.Fill(ds, "Persoane");
                                dataGridViewChild.DataSource = ds.Tables["Persoane"];
                                MessageBox.Show("Persoana a fost stearsa cu succes!");

                                childId = -1;
                                parentId = -1;
                                connection.Close();
                            }
                        }
                        catch (Exception ex)
                        {
                            MessageBox.Show(ex.Message);
                        }
                    }
                    else
                    {
                        MessageBox.Show("Alegeti o persoana!");
                    }
                }

        private void dataGridViewChild_SelectionChanged(object sender, EventArgs e)
        {
            DataGridView dgv = sender as DataGridView;
            if (dgv != null && dgv.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedEntry = dgv.SelectedRows[0];
                if (selectedEntry != null)
                {
                    childId = (int)selectedEntry.Cells[0].Value;
                    textBoxNume.Text = selectedEntry.Cells[1].Value.ToString();
                    textBoxPrenume.Text = selectedEntry.Cells[2].Value.ToString();
                    textBoxEmail.Text = selectedEntry.Cells[3].Value.ToString();
                   
                }
            }
        }


        private void buttonAdd_Click(object sender, EventArgs e)
        {
            try
            {
                string nume = textBoxNume.Text;
                string prenume = textBoxPrenume.Text;
                string email = textBoxEmail.Text;
                int aid = int.Parse(dataGridViewParent.SelectedRows[0].Cells[0].Value.ToString());

                if (textBoxNume.Text.Length != 0 && textBoxPrenume.Text.Length != 0 && textBoxEmail.Text.Length != 0 && aid > 0)
                {
                    try
                    {
                        using (SqlConnection connection = new SqlConnection(connectionString))
                        {
                            connection.Open();
                            adapter.InsertCommand = new SqlCommand("INSERT INTO Persoane (NUME, Prenume, Email, Aid) VALUES" +
                                "(@nume,@prenume,@email,@aid);", connection);
                            adapter.InsertCommand.Parameters.AddWithValue("@nume", nume);
                            adapter.InsertCommand.Parameters.AddWithValue("@prenume", prenume);
                            adapter.InsertCommand.Parameters.AddWithValue("@email", email);
                            adapter.InsertCommand.Parameters.AddWithValue("@aid", aid);
                            adapter.InsertCommand.ExecuteNonQuery();

                            adapter.SelectCommand = new SqlCommand("SELECT * FROM Persoane WHERE Aid=@aid;", connection);
                            adapter.SelectCommand.Parameters.AddWithValue("@aid", aid);
                            ds.Tables["Persoane"].Clear();
                            adapter.Fill(ds, "Persoane");
                            dataGridViewChild.DataSource = ds.Tables["Persoane"];

                            MessageBox.Show("Persoana adaugata cu succes!");

                            connection.Close();
                        }
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show(ex.Message);
                    }
                }
                else
                {
                    MessageBox.Show("Date incorecte.");
                }
            }
            catch (System.FormatException)
            {
                MessageBox.Show("Date incorecte.");
            }

        }

        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            try
            {
                int pid = childId;
                string nume = textBoxNume.Text;
                string prenume = textBoxPrenume.Text;
                string email = textBoxEmail.Text;


                if (textBoxNume.Text.Length == 0 || textBoxPrenume.Text.Length == 0 || textBoxEmail.Text.Length == 0) { MessageBox.Show("Date incorecte."); }
                else
                {
                    try
                    {
                        using (SqlConnection connection = new SqlConnection(connectionString))
                        {
                            connection.Open();
                            adapter.UpdateCommand = new SqlCommand("UPDATE Persoane SET Nume = @nume, Prenume = @prenume, Email = @email WHERE Pid=@pid", connection);
                            adapter.UpdateCommand.Parameters.AddWithValue("@nume", nume);
                            adapter.UpdateCommand.Parameters.AddWithValue("@prenume", prenume);
                            adapter.UpdateCommand.Parameters.AddWithValue("@email", email);
                            adapter.UpdateCommand.Parameters.AddWithValue("@pid", pid);
                            adapter.UpdateCommand.ExecuteNonQuery();

                            adapter.SelectCommand = new SqlCommand("SELECT * FROM Persoane WHERE Aid=@aid;", connection);
                            adapter.SelectCommand.Parameters.AddWithValue("@aid", parentId);
                            ds.Tables["Persoane"].Clear();
                            adapter.Fill(ds, "Persoane");
                            dataGridViewChild.DataSource = ds.Tables["Persoane"];
                            childId = -1;
                            MessageBox.Show("Modificare executata cu succes!");

                            connection.Close();
                        }
                    }
                    catch (Exception ex)
                    {
                        MessageBox.Show(ex.Message);
                    }
                }
            }
            catch (System.FormatException)
            {
                MessageBox.Show("Date incorecte.");
            }
        }

    }
}
