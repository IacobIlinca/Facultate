namespace Lab1SGBD_V2
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dataGridViewParent = new System.Windows.Forms.DataGridView();
            this.dataGridViewChild = new System.Windows.Forms.DataGridView();
            this.buttonDel = new System.Windows.Forms.Button();
            this.nume = new System.Windows.Forms.Label();
            this.textBoxNume = new System.Windows.Forms.TextBox();
            this.textBoxPrenume = new System.Windows.Forms.TextBox();
            this.textBoxEmail = new System.Windows.Forms.TextBox();
            this.prenume = new System.Windows.Forms.Label();
            this.email = new System.Windows.Forms.Label();
            this.buttonAdd = new System.Windows.Forms.Button();
            this.buttonUpdate = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridViewParent
            // 
            this.dataGridViewParent.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewParent.Location = new System.Drawing.Point(12, 12);
            this.dataGridViewParent.Name = "dataGridViewParent";
            this.dataGridViewParent.RowHeadersWidth = 62;
            this.dataGridViewParent.RowTemplate.Height = 33;
            this.dataGridViewParent.Size = new System.Drawing.Size(472, 384);
            this.dataGridViewParent.TabIndex = 0;
            this.dataGridViewParent.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView1_CellContentClick);
            this.dataGridViewParent.SelectionChanged += new System.EventHandler(this.dataGridViewParent_SelectionChanged);
            // 
            // dataGridViewChild
            // 
            this.dataGridViewChild.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewChild.Location = new System.Drawing.Point(792, 19);
            this.dataGridViewChild.Name = "dataGridViewChild";
            this.dataGridViewChild.RowHeadersWidth = 62;
            this.dataGridViewChild.RowTemplate.Height = 33;
            this.dataGridViewChild.Size = new System.Drawing.Size(499, 377);
            this.dataGridViewChild.TabIndex = 2;
            this.dataGridViewChild.SelectionChanged += new System.EventHandler(this.dataGridViewChild_SelectionChanged);
            // 
            // buttonDel
            // 
            this.buttonDel.Location = new System.Drawing.Point(1016, 402);
            this.buttonDel.Name = "buttonDel";
            this.buttonDel.Size = new System.Drawing.Size(112, 34);
            this.buttonDel.TabIndex = 3;
            this.buttonDel.Text = "Delete";
            this.buttonDel.UseVisualStyleBackColor = true;
            this.buttonDel.Click += new System.EventHandler(this.buttonDel_Click);
            // 
            // nume
            // 
            this.nume.AutoSize = true;
            this.nume.Location = new System.Drawing.Point(495, 33);
            this.nume.Name = "nume";
            this.nume.Size = new System.Drawing.Size(69, 25);
            this.nume.TabIndex = 4;
            this.nume.Text = "Nume: ";
            // 
            // textBoxNume
            // 
            this.textBoxNume.Location = new System.Drawing.Point(587, 33);
            this.textBoxNume.Name = "textBoxNume";
            this.textBoxNume.Size = new System.Drawing.Size(150, 31);
            this.textBoxNume.TabIndex = 5;
            // 
            // textBoxPrenume
            // 
            this.textBoxPrenume.Location = new System.Drawing.Point(587, 95);
            this.textBoxPrenume.Name = "textBoxPrenume";
            this.textBoxPrenume.Size = new System.Drawing.Size(150, 31);
            this.textBoxPrenume.TabIndex = 6;
            // 
            // textBoxEmail
            // 
            this.textBoxEmail.Location = new System.Drawing.Point(587, 157);
            this.textBoxEmail.Name = "textBoxEmail";
            this.textBoxEmail.Size = new System.Drawing.Size(150, 31);
            this.textBoxEmail.TabIndex = 7;
            // 
            // prenume
            // 
            this.prenume.AutoSize = true;
            this.prenume.Location = new System.Drawing.Point(495, 98);
            this.prenume.Name = "prenume";
            this.prenume.Size = new System.Drawing.Size(86, 25);
            this.prenume.TabIndex = 8;
            this.prenume.Text = "Prenume:";
            // 
            // email
            // 
            this.email.AutoSize = true;
            this.email.Location = new System.Drawing.Point(505, 155);
            this.email.Name = "email";
            this.email.Size = new System.Drawing.Size(63, 25);
            this.email.TabIndex = 9;
            this.email.Text = "Email: ";
            // 
            // buttonAdd
            // 
            this.buttonAdd.Location = new System.Drawing.Point(558, 219);
            this.buttonAdd.Name = "buttonAdd";
            this.buttonAdd.Size = new System.Drawing.Size(112, 34);
            this.buttonAdd.TabIndex = 10;
            this.buttonAdd.Text = "Add";
            this.buttonAdd.UseVisualStyleBackColor = true;
            this.buttonAdd.Click += new System.EventHandler(this.buttonAdd_Click);
            // 
            // buttonUpdate
            // 
            this.buttonUpdate.Location = new System.Drawing.Point(558, 279);
            this.buttonUpdate.Name = "buttonUpdate";
            this.buttonUpdate.Size = new System.Drawing.Size(112, 34);
            this.buttonUpdate.TabIndex = 11;
            this.buttonUpdate.Text = "Update";
            this.buttonUpdate.UseVisualStyleBackColor = true;
            this.buttonUpdate.Click += new System.EventHandler(this.buttonUpdate_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1376, 450);
            this.Controls.Add(this.buttonUpdate);
            this.Controls.Add(this.buttonAdd);
            this.Controls.Add(this.email);
            this.Controls.Add(this.prenume);
            this.Controls.Add(this.textBoxEmail);
            this.Controls.Add(this.textBoxPrenume);
            this.Controls.Add(this.textBoxNume);
            this.Controls.Add(this.nume);
            this.Controls.Add(this.buttonDel);
            this.Controls.Add(this.dataGridViewChild);
            this.Controls.Add(this.dataGridViewParent);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private DataGridView dataGridViewParent;
        private DataGridView dataGridViewChild;
        private Button buttonDel;
        private Label nume;
        private TextBox textBoxNume;
        private TextBox textBoxPrenume;
        private TextBox textBoxEmail;
        private Label prenume;
        private Label email;
        private Button buttonAdd;
        private Button buttonUpdate;
    }
}