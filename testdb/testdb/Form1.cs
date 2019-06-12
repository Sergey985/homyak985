using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;

namespace testdb
{
    public partial class Form1 : Form
    {
        private string _connectionString = "Server=127.0.0.1;Port=3306;Database=sunshine;Uid=root;Pwd=sistem32;Command Timeout=99999";
        private MySqlConnection _mysqlConnection;

        public string english;
        public string german;
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            check();
        }

        private void check()
        {
            if (textBox2.Text != null)
            {
                if (textBox2.Text != english)
                {
                    textBox2.Font = new Font("Tahoma", 11);
                    textBox2.ForeColor = Color.Red;
                    textBox2.Text = english;
                }
                else
                {
                    textBox2.Text = english;
                }
            }

            if (textBox1.Text != null)
            {
                if (textBox1.Text != german)
                {
                    textBox1.Font = new Font("Tahoma", 11);
                    textBox1.ForeColor = Color.Red;
                    textBox1.Text = german;
                }
                else
                {
                    textBox1.Text = german;
                }
            }



        }

        private void Form1_Load(object sender, EventArgs e)
        {
            popup f2 = new popup();
            f2.Close();
            load();

        }

    

        private void load()
        {
         
            _mysqlConnection = new MySqlConnection(_connectionString);
            Exception aException = new Exception();

            string sQuery = "select * from sunshine.lang order by rand() limit 1";
            string sName;
            string en;
            string de;
            DataTable aTable = GetData(sQuery, out aException);
            label1.Text = "";
            foreach (DataRow aRow in aTable.Rows)
            {
                sName = aRow["RU"].ToString();
                label1.Text = sName;
            }
            foreach (DataRow aRow in aTable.Rows)
            {
                en = aRow["Eng"].ToString();
                english = en;
            }
            foreach (DataRow aRow in aTable.Rows)
            {
                de = aRow["DE"].ToString();
                german = de;
            }
        }
        private DataTable GetData(string selectCmd, out Exception ex)
        {
            try
            {
                lock (_mysqlConnection)
                {
                    if (_mysqlConnection.State != ConnectionState.Open)
                        _mysqlConnection.Open();
                    MySqlDataAdapter ta = new MySqlDataAdapter(selectCmd, _mysqlConnection);
                    DataTable dt = new DataTable();
                    ta.Fill(dt);
                    ex = null;
                    return dt;
                }
            }
            catch
            {
                ex = null;
                return null;
            }

        }

        private void button2_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void fileToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void addNewWordsToolStripMenuItem_Click(object sender, EventArgs e)
        {
            
            AddNewEl f2= new AddNewEl();
            f2.Show();
           
        }

        private void button3_Click(object sender, EventArgs e)
        {
            textBox2.Text = "";
            textBox1.Text = "";

            load();

        }

        private void toolsToolStripMenuItem_Click(object sender, EventArgs e)
        {

        }

        private void toolsToolStripMenuItem1_Click(object sender, EventArgs e)
        {
            Language f3 = new Language();
            f3.Show();
           

        }

    }
}
