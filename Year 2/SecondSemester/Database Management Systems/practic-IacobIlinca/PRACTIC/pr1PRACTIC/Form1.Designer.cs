namespace pr1PRACTIC
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
            this.nume = new System.Windows.Forms.Label();
            this.prenume = new System.Windows.Forms.Label();
            this.gen = new System.Windows.Forms.Label();
            this.textBoxNume = new System.Windows.Forms.TextBox();
            this.textBoxPrenume = new System.Windows.Forms.TextBox();
            this.textBoxGen = new System.Windows.Forms.TextBox();
            this.buttonAdd = new System.Windows.Forms.Button();
            this.buttonUpdate = new System.Windows.Forms.Button();
            this.buttonDelete = new System.Windows.Forms.Button();
            this.varsta = new System.Windows.Forms.Label();
            this.textBoxVarsta = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridViewParent
            // 
            this.dataGridViewParent.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewParent.Location = new System.Drawing.Point(12, 71);
            this.dataGridViewParent.Name = "dataGridViewParent";
            this.dataGridViewParent.RowHeadersWidth = 62;
            this.dataGridViewParent.RowTemplate.Height = 33;
            this.dataGridViewParent.Size = new System.Drawing.Size(518, 317);
            this.dataGridViewParent.TabIndex = 0;
            this.dataGridViewParent.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView1_CellContentClick);
            this.dataGridViewParent.SelectionChanged += new System.EventHandler(this.dataGridViewParent_SelectionChanged);
            // 
            // dataGridViewChild
            // 
            this.dataGridViewChild.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewChild.Location = new System.Drawing.Point(895, 71);
            this.dataGridViewChild.Name = "dataGridViewChild";
            this.dataGridViewChild.RowHeadersWidth = 62;
            this.dataGridViewChild.RowTemplate.Height = 33;
            this.dataGridViewChild.Size = new System.Drawing.Size(477, 317);
            this.dataGridViewChild.TabIndex = 1;
            this.dataGridViewChild.SelectionChanged += new System.EventHandler(this.dataGridViewChild_SelectionChanged);
            // 
            // nume
            // 
            this.nume.AutoSize = true;
            this.nume.Location = new System.Drawing.Point(536, 86);
            this.nume.Name = "nume";
            this.nume.Size = new System.Drawing.Size(60, 25);
            this.nume.TabIndex = 2;
            this.nume.Text = "Nume";
            this.nume.Click += new System.EventHandler(this.label1_Click);
            // 
            // prenume
            // 
            this.prenume.AutoSize = true;
            this.prenume.Location = new System.Drawing.Point(536, 149);
            this.prenume.Name = "prenume";
            this.prenume.Size = new System.Drawing.Size(82, 25);
            this.prenume.TabIndex = 3;
            this.prenume.Text = "Prenume";
            this.prenume.Click += new System.EventHandler(this.nr_calorii_Click);
            // 
            // gen
            // 
            this.gen.AutoSize = true;
            this.gen.Location = new System.Drawing.Point(550, 214);
            this.gen.Name = "gen";
            this.gen.Size = new System.Drawing.Size(43, 25);
            this.gen.TabIndex = 4;
            this.gen.Text = "Gen";
            this.gen.Click += new System.EventHandler(this.pret_Click);
            // 
            // textBoxNume
            // 
            this.textBoxNume.Location = new System.Drawing.Point(685, 91);
            this.textBoxNume.Name = "textBoxNume";
            this.textBoxNume.Size = new System.Drawing.Size(150, 31);
            this.textBoxNume.TabIndex = 5;
            // 
            // textBoxPrenume
            // 
            this.textBoxPrenume.Location = new System.Drawing.Point(685, 149);
            this.textBoxPrenume.Name = "textBoxPrenume";
            this.textBoxPrenume.Size = new System.Drawing.Size(150, 31);
            this.textBoxPrenume.TabIndex = 6;
            // 
            // textBoxGen
            // 
            this.textBoxGen.Location = new System.Drawing.Point(685, 208);
            this.textBoxGen.Name = "textBoxGen";
            this.textBoxGen.Size = new System.Drawing.Size(150, 31);
            this.textBoxGen.TabIndex = 7;
            // 
            // buttonAdd
            // 
            this.buttonAdd.Location = new System.Drawing.Point(650, 378);
            this.buttonAdd.Name = "buttonAdd";
            this.buttonAdd.Size = new System.Drawing.Size(112, 34);
            this.buttonAdd.TabIndex = 8;
            this.buttonAdd.Text = "Add";
            this.buttonAdd.UseVisualStyleBackColor = true;
            this.buttonAdd.Click += new System.EventHandler(this.buttonAdd_Click);
            // 
            // buttonUpdate
            // 
            this.buttonUpdate.Location = new System.Drawing.Point(650, 442);
            this.buttonUpdate.Name = "buttonUpdate";
            this.buttonUpdate.Size = new System.Drawing.Size(112, 34);
            this.buttonUpdate.TabIndex = 9;
            this.buttonUpdate.Text = "Update";
            this.buttonUpdate.UseVisualStyleBackColor = true;
            this.buttonUpdate.Click += new System.EventHandler(this.buttonUpdate_Click);
            // 
            // buttonDelete
            // 
            this.buttonDelete.Location = new System.Drawing.Point(1096, 442);
            this.buttonDelete.Name = "buttonDelete";
            this.buttonDelete.Size = new System.Drawing.Size(112, 34);
            this.buttonDelete.TabIndex = 10;
            this.buttonDelete.Text = "Delete";
            this.buttonDelete.UseVisualStyleBackColor = true;
            this.buttonDelete.Click += new System.EventHandler(this.buttonDel_Click);
            // 
            // varsta
            // 
            this.varsta.AutoSize = true;
            this.varsta.Location = new System.Drawing.Point(550, 292);
            this.varsta.Name = "varsta";
            this.varsta.Size = new System.Drawing.Size(60, 25);
            this.varsta.TabIndex = 11;
            this.varsta.Text = "Varsta";
            // 
            // textBoxVarsta
            // 
            this.textBoxVarsta.Location = new System.Drawing.Point(685, 286);
            this.textBoxVarsta.Name = "textBoxVarsta";
            this.textBoxVarsta.Size = new System.Drawing.Size(167, 31);
            this.textBoxVarsta.TabIndex = 12;
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(10F, 25F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1384, 547);
            this.Controls.Add(this.textBoxVarsta);
            this.Controls.Add(this.varsta);
            this.Controls.Add(this.buttonDelete);
            this.Controls.Add(this.buttonUpdate);
            this.Controls.Add(this.buttonAdd);
            this.Controls.Add(this.textBoxGen);
            this.Controls.Add(this.textBoxPrenume);
            this.Controls.Add(this.textBoxNume);
            this.Controls.Add(this.gen);
            this.Controls.Add(this.prenume);
            this.Controls.Add(this.nume);
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
        private Label nume;
        private Label prenume;
        private Label gen;
        private TextBox textBoxNume;
        private TextBox textBoxPrenume;
        private TextBox textBoxGen;
        private Button buttonAdd;
        private Button buttonUpdate;
        private Button buttonDelete;
        private Label varsta;
        private TextBox textBoxVarsta;
    }
}