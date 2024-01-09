using Microsoft.Data.SqlClient;
using System.Data;
namespace pr1PRACTIC
{
    public partial class Form1 : Form
    {
        //schimba numele la bd
        string connectionString = "Data Source=LAPTOP-MF0S35KN\\SQLEXPRESS;Initial Catalog=S9;Integrated Security=True;TrustServerCertificate=True";
        DataSet ds = new DataSet();
        SqlDataAdapter adapter = new SqlDataAdapter();
        int parentId = -1;
        int childId = -1;


        public Form1()
        {
            InitializeComponent();
        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void pret_Click(object sender, EventArgs e)
        {

        }

        public void getParentList()
        {
            try
            {
                using (SqlConnection connection = new SqlConnection(connectionString))
                {
                    connection.Open();
                    //parent table
                    adapter.SelectCommand = new SqlCommand("Select * FROM InghetatePreferate", connection);
                    adapter.Fill(ds, "InghetatePreferate");
                    parentId = -1;
                    dataGridViewParent.DataSource = ds.Tables["InghetatePreferate"];
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
                    //child table
                    adapter.SelectCommand = new SqlCommand("Select * FROM Copii", connection);
                    adapter.Fill(ds, "Copii");
                    childId = -1;
                    dataGridViewChild.DataSource = ds.Tables["Copii"];
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
                            //aici schimba
                            adapter.SelectCommand = new SqlCommand("Select * FROM Copii where IPid=@idSelectat;", connection);
                            adapter.SelectCommand.Parameters.AddWithValue("@idSelectat", selected.Cells[0].Value);
                            if (ds.Tables["Copii"] is not null)
                            {
                                ds.Tables["Copii"].Clear();
                            }
                            adapter.Fill(ds, "Copii");
                            childId = -1;
                            dataGridViewChild.DataSource = ds.Tables["Copii"];
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
                        adapter.DeleteCommand = new SqlCommand("DELETE FROM Copii WHERE Cid=@Cid;", connection);
                        adapter.DeleteCommand.Parameters.AddWithValue("@Cid", childId);
                        adapter.DeleteCommand.ExecuteNonQuery();

                        adapter.SelectCommand = new SqlCommand("SELECT * FROM Copii WHERE IPid=@IPid;", connection);
                        adapter.SelectCommand.Parameters.AddWithValue("@IPid", parentId);
                        ds.Tables["Copii"].Clear();
                        adapter.Fill(ds, "Copii");
                        dataGridViewChild.DataSource = ds.Tables["Copii"];
                        MessageBox.Show("Copilul a fost sters cu succes!");

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
                MessageBox.Show("Alegeti un copil!");
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
                    //vf aici
                    childId = (int)selectedEntry.Cells[0].Value;
                    textBoxNume.Text = selectedEntry.Cells[1].Value.ToString();
                    textBoxPrenume.Text = selectedEntry.Cells[2].Value.ToString();
                    textBoxGen.Text = selectedEntry.Cells[3].Value.ToString();
                    textBoxVarsta.Text = selectedEntry.Cells[4].Value.ToString();
                }
            }
        }

        private void buttonAdd_Click(object sender, EventArgs e)
        {
            try
            {
                string nume = textBoxNume.Text;
                string prenume = textBoxPrenume.Text;
                string gen = textBoxGen.Text;
                string varsta = textBoxVarsta.Text;
                int IPid = int.Parse(dataGridViewParent.SelectedRows[0].Cells[0].Value.ToString());

                if (textBoxNume.Text.Length != 0 && textBoxPrenume.Text.Length != 0 && textBoxGen.Text.Length != 0 && textBoxVarsta.Text.Length != 0 && IPid > 0)
                {
                    try
                    {
                        using (SqlConnection connection = new SqlConnection(connectionString))
                        {
                            connection.Open();
                            adapter.InsertCommand = new SqlCommand("INSERT INTO Copii (nume, prenume, gen,varsta, IPid) VALUES" +
                                "(@nume,@prenume,@gen,@varsta,@IPid);", connection);
                            adapter.InsertCommand.Parameters.AddWithValue("@nume", nume);
                            adapter.InsertCommand.Parameters.AddWithValue("@prenume", prenume);
                            adapter.InsertCommand.Parameters.AddWithValue("@gen", gen);
                            adapter.InsertCommand.Parameters.AddWithValue("@varsta", varsta);
                            adapter.InsertCommand.Parameters.AddWithValue("@IPid", IPid);
                            adapter.InsertCommand.ExecuteNonQuery();

                            adapter.SelectCommand = new SqlCommand("SELECT * FROM Copii WHERE IPid=@IPid;", connection);
                            adapter.SelectCommand.Parameters.AddWithValue("@IPid", IPid);
                            ds.Tables["Copii"].Clear();
                            adapter.Fill(ds, "Copii");
                            dataGridViewChild.DataSource = ds.Tables["Copii"];

                            MessageBox.Show("Copil adaugat cu succes!");

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
                int Cid = childId;
                string nume = textBoxNume.Text;
                string prenume = textBoxPrenume.Text;
                string gen = textBoxGen.Text;
                string varsta = textBoxVarsta.Text;


                if (textBoxNume.Text.Length == 0 || textBoxPrenume.Text.Length == 0 || textBoxGen.Text.Length == 0 || textBoxVarsta.Text.Length == 0) { MessageBox.Show("Date incorecte."); }
                else
                {
                    try
                    {
                        using (SqlConnection connection = new SqlConnection(connectionString))
                        {
                            connection.Open();
                            adapter.UpdateCommand = new SqlCommand("UPDATE Copii SET nume = @nume, prenume = @prenume, gen = @gen, varsta=@varsta WHERE Cid=@Cid", connection);
                            adapter.UpdateCommand.Parameters.AddWithValue("@nume", nume);
                            adapter.UpdateCommand.Parameters.AddWithValue("@prenume", prenume);
                            adapter.UpdateCommand.Parameters.AddWithValue("@gen", gen);
                            adapter.UpdateCommand.Parameters.AddWithValue("@varsta", varsta);
                            adapter.UpdateCommand.Parameters.AddWithValue("@Cid", Cid);
                            adapter.UpdateCommand.ExecuteNonQuery();

                            adapter.SelectCommand = new SqlCommand("SELECT * FROM Copii WHERE IPid=@IPid;", connection);
                            adapter.SelectCommand.Parameters.AddWithValue("@IPid", parentId);
                            ds.Tables["Copii"].Clear();
                            adapter.Fill(ds, "Copii");
                            dataGridViewChild.DataSource = ds.Tables["Copii"];
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

        private void nr_calorii_Click(object sender, EventArgs e)
        {

        }
    }
}