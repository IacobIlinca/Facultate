using Microsoft.Data.SqlClient;
using System.Data;
using System.Configuration;
namespace Lab1SGBD_V2
{
    public partial class Form1 : Form
    {
        //string connectionString = "Data Source=LAPTOP-MF0S35KN\\SQLEXPRESS;Initial Catalog=Biblioteca;Integrated Security=True;TrustServerCertificate=True";
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

                string connectionString = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;
                SqlConnection connection = new SqlConnection(connectionString);
                string parentTable = ConfigurationManager.AppSettings["ParentTableName"];
                adapter.SelectCommand = new SqlCommand("Select * FROM " + parentTable, connection);
                adapter.Fill(ds, parentTable);
                dataGridViewParent.DataSource = ds.Tables[parentTable];

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
                if (dataGridViewParent.SelectedCells.Count > 0)
                {
                    string pkParent = dataGridViewParent.CurrentRow.Cells[0].Value.ToString();
                    string connectionString = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;
                    SqlConnection conn = new SqlConnection(connectionString);
                    string childTable = ConfigurationManager.AppSettings["ChildTableName"];
                    string fkStatement = ConfigurationManager.AppSettings["pk_parent"];
                    adapter.SelectCommand = new SqlCommand("SELECT * FROM " + childTable + " WHERE " + fkStatement, conn);
                    adapter.SelectCommand.Parameters.AddWithValue("@Parent", pkParent);
                    if (ds.Tables[childTable] != null)
                        ds.Tables[childTable].Clear();
                    adapter.Fill(ds, childTable);
                    dataGridViewChild.DataSource = ds.Tables[childTable];
                }
            }
            catch (Exception e)
            {
                MessageBox.Show(e.Message);
            }
        }



        //private void dataGridViewParent_SelectionChanged(object sender, EventArgs e)
        //{
        //    parentId = -1;
        //    childId = -1;
        //    DataGridView gridView = sender as DataGridView;
        //    if (gridView != null && gridView.SelectedRows.Count > 0)
        //    {
        //        DataGridViewRow selected = gridView.SelectedRows[0];
        //        parentId = (int)selected.Cells[0].Value;

        //        if (selected != null)
        //        {
        //            try
        //            {
        //                using (SqlConnection connection = new SqlConnection(connectionString))
        //                {
        //                    connection.Open();
        //                    adapter.SelectCommand = new SqlCommand("Select * FROM Persoane where Aid=@idSelectat;", connection);
        //                    adapter.SelectCommand.Parameters.AddWithValue("@idSelectat", selected.Cells[0].Value);
        //                    if (ds.Tables["Persoane"] is not null)
        //                    {
        //                        ds.Tables["Persoane"].Clear();
        //                    }
        //                    adapter.Fill(ds, "Persoane");
        //                    childId = -1;
        //                    dataGridViewChild.DataSource = ds.Tables["Persoane"];
        //                    connection.Close();
        //                }
        //            }
        //            catch (Exception ex)
        //            {
        //                MessageBox.Show(ex.Message);
        //            }
        //        }
        //    }
        //}

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            getChildList();
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            getParentList();
            loadTextBoxes();
            //getChildList();
        }

        public void loadTextBoxes()
        {
            panel1.Controls.Clear();
            List<string> childColumnsList = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));
            int textboxCount = Convert.ToInt32(ConfigurationManager.AppSettings["textbox_count"]);
            int locationTextBox = 50;
            int locationLabel = 50;
            int index = 1;
            while (index <= textboxCount)
            {
                Label label = new Label();
                TextBox textBox = new TextBox();
                label.Location = new Point(0, locationLabel);
                textBox.Location = new Point(100, locationTextBox);
                textBox.Name = childColumnsList[index - 1];
                //Console.WriteLine(textBox.Name);
                label.Text = ConfigurationManager.AppSettings["label" + index.ToString()];
                // Console.WriteLine(label.Text);
                panel1.Controls.Add(label);
                panel1.Controls.Add(textBox);
                locationTextBox += textBox.Height + 10;
                locationLabel += label.Height + 10;
                index++;
            }
        }

        private void buttonDel_Click(object sender, EventArgs e)
        {

            //childId = int.Parse(dataGridViewChild.SelectedRows[0].Cells[0].Value.ToString());
            try
            {
                if (dataGridViewChild.SelectedCells.Count > 0)
                {
                    string pkChild = dataGridViewChild.CurrentRow.Cells[0].Value.ToString();
                    string childTable = ConfigurationManager.AppSettings["ChildTableName"];
                    string pkStatement = ConfigurationManager.AppSettings["pk_child"];
                    string connectionString = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;
                    SqlConnection conn = new SqlConnection(connectionString);
                    conn.Open();

                    SqlCommand cmd = new SqlCommand("DELETE FROM " + childTable + " WHERE " + pkStatement, conn);
                    cmd.Parameters.AddWithValue("@Child", pkChild);
                    cmd.ExecuteNonQuery();
                    getChildList();
                    MessageBox.Show("Deleted item succesfully!");
                    conn.Close();
                }
                else
                {
                    MessageBox.Show("Plese select a child record");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }

        }

        //private void dataGridViewChild_SelectionChanged(object sender, EventArgs e)
        //{
        //    DataGridView dgv = sender as DataGridView;
        //    if (dgv != null && dgv.SelectedRows.Count > 0)
        //    {
        //        DataGridViewRow selectedEntry = dgv.SelectedRows[0];
        //        if (selectedEntry != null)
        //        {
        //            childId = (int)selectedEntry.Cells[0].Value;
        //            textBoxNume.Text = selectedEntry.Cells[1].Value.ToString();
        //            textBoxPrenume.Text = selectedEntry.Cells[2].Value.ToString();
        //            textBoxEmail.Text = selectedEntry.Cells[3].Value.ToString();

        //        }
        //    }
        //}


        private void buttonAdd_Click(object sender, EventArgs e)
        {
            try
            {
                string parentKey = ConfigurationManager.AppSettings["parentKey"];
                string childTable = ConfigurationManager.AppSettings["ChildTableName"];
                string insertedParametersNames = ConfigurationManager.AppSettings["InsertedParametersNames"];
                string childColumnNames = ConfigurationManager.AppSettings["InsertNames"];
                List<string> childColumnsList = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));
                string connectionString = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;
                SqlConnection conn = new SqlConnection(connectionString);
                conn.Open();

                if (dataGridViewParent.SelectedCells.Count > 0)
                {
                    string idd = dataGridViewParent.CurrentRow.Cells[0].Value.ToString();
                    SqlCommand cmd = new SqlCommand("INSERT INTO " + childTable + " (" + childColumnNames + ") VALUES (" + insertedParametersNames + ")", conn);
                    foreach (string parameter in childColumnsList)
                    {
                        TextBox textBox = (TextBox)panel1.Controls[parameter];
                        if (string.IsNullOrWhiteSpace(textBox.Text))
                        {
                            MessageBox.Show("Invalid!");
                            return;
                        }
                        if (!parameter.Equals(parentKey))
                        {
                            cmd.Parameters.AddWithValue("@" + parameter, textBox.Text);
                        }
                    }
                    cmd.Parameters.AddWithValue("@" + parentKey, idd);

                    cmd.ExecuteNonQuery();
                    getChildList();
                    MessageBox.Show("Record inserted succesfully!");
                    //ds.Clear();
                    //adapter.Fill(ds);
                    conn.Close();
                }
                else
                {
                    MessageBox.Show("Plese select a parent record");
                }

            }
            catch (Exception ex)
            {
                MessageBox.Show("Error: " + ex.Message);
            }

        }

        private void buttonUpdate_Click(object sender, EventArgs e)
        {
            try
            {
                if (dataGridViewChild.SelectedCells.Count > 0)
                {
                    string pkChild = dataGridViewChild.CurrentRow.Cells[0].Value.ToString();
                    string childTable = ConfigurationManager.AppSettings["ChildTableName"];

                    List<string> childColumnsList = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));
                    string updateColumns = ConfigurationManager.AppSettings["UpdateColumns"];
                    string connectionString = ConfigurationManager.ConnectionStrings["cn"].ConnectionString;
                    SqlConnection conn = new SqlConnection(connectionString);
                    conn.Open();
                    SqlCommand cmd = new SqlCommand("Update " + childTable + " SET " + updateColumns, conn);
                    cmd.Parameters.AddWithValue("@id", pkChild);
                    foreach (string column in childColumnsList)
                    {
                        TextBox textBox = (TextBox)panel1.Controls[column];
                        if (string.IsNullOrWhiteSpace(textBox.Text))
                        {
                            MessageBox.Show("Invalid!");
                            return;
                        }
                        cmd.Parameters.AddWithValue("@" + column, textBox.Text);
                    }
                    
                    cmd.ExecuteNonQuery();
                    getChildList();
                    MessageBox.Show("Updated item succesfully!");
                    conn.Close();
                }
                else
                {
                    MessageBox.Show("Plese select a child record");
                }

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        }

        private void dataGridViewChild_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {
            try
            {
                if (dataGridViewChild.SelectedCells.Count > 0)
                {
                    int index = dataGridViewChild.CurrentCell.RowIndex;
                    string childTable = ConfigurationManager.AppSettings["ChildTableName"];
                    List<string> childColumnsList = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));

                    foreach (string col in childColumnsList)
                    {
                        TextBox textBox = (TextBox)panel1.Controls[col];
                        textBox.Text = ds.Tables[childTable].Rows[index][col].ToString();
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
            }
        
        }
    }
}
