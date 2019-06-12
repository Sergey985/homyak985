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
    public partial class AddNewEl : Form
    {
        private string _connectionString = "Server=127.0.0.1;Port=3306;Database=sunshine;Uid=root;Pwd=sistem32;Command Timeout=99999; charset = utf8;";
        private MySqlConnection _mysqlConnection;


        public AddNewEl()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {   
            ActiveForm.Hide(); 
        }
        string eng, ru, de;
        private void button1_Click(object sender, EventArgs e)
        {
            if ((textBox1.Text == "") || (textBox2.Text == "") || (textBox3.Text == ""))
            {
                label4.Text = "You should fill all fields";
                label4.ForeColor = Color.Red;
            }
            else
            {
                _mysqlConnection = new MySqlConnection(_connectionString);
                Exception aException = new Exception();
                string sQuery = "SELECT ID FROM sunshine.lang ORDER BY ID DESC LIMIT 1";
                try
                {
                    lock (_mysqlConnection)
                    {
                        if (_mysqlConnection.State != ConnectionState.Open)
                            _mysqlConnection.Open();
                        MySqlDataAdapter ta = new MySqlDataAdapter(sQuery, _mysqlConnection);


                        DataTable ds = new DataTable();
                        ta.Fill(ds);
                        //string a = "0";
                        //      DataTable aTable = GetData(sQuery, out aException);
                        //     foreach (DataRow aRow in aTable.Rows)
                        //   {
                        string sName = ds.Rows[0]["ID"].ToString();
                        //     a = sName;
                        // }
                        int i = Convert.ToInt32(sName);
                        i++;

                    //    eng = textBox1.Text;
                 //       de = textBox2.Text;
                 //       ru = textBox3.Text;
                        MySqlCommand cmd = new MySqlCommand("", _mysqlConnection);
                          string sSQL = string.Format("INSERT INTO lang (ID, Eng, DE, RU) VALUES ({0}, '{1}', '{2}', '{3}');"
                                                      , i
                                                      , textBox1.Text
                                                      , textBox2.Text
                                                      , textBox3.Text
                                                      );
                     //  string sSQL = string.Format("INSERT INTO sunshine.lang (ID, Eng, DE, RU) VALUES (i, eng, de, ru);");


                        cmd.CommandText = sSQL;

                        cmd.ExecuteNonQuery();

                        textBox1.Text = "";
                        textBox2.Text = "";
                        textBox3.Text = "";
                    }
                }
                catch
                {
                    aException = null;
                    //return null;
                }







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

        private void AddNewEl_Load(object sender, EventArgs e)
        {
            Form1 f1 = new Form1();
            f1.Visible = false;
        }
    }
}
