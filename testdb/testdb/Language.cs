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
    public partial class Language : Form
    {

        private string _connectionString = "Server=127.0.0.1;Port=3306;Database=sunshine;Uid=root;Pwd=sistem32;Command Timeout=99999; charset = utf8;";
        private MySqlConnection _mysqlConnection;

        public Language()
        {
            InitializeComponent();
        }

        private void button2_Click(object sender, EventArgs e)
        {
            ActiveForm.Hide();
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
        private void Apply_Click(object sender, EventArgs e)
        {
            _mysqlConnection = new MySqlConnection(_connectionString);
            Exception aException = new Exception();
            _mysqlConnection.Open();
          
           // string eng = "";
           // string ru = "";
           // string de = "";
            MySqlCommand cmd = new MySqlCommand("", _mysqlConnection);
      
            if (comboBox1.Text == "English")
            { 
            
             string sSQL = string.Format("UPDATE sunshine.idlang SET de = 0, eng = 1, ru = 0 LIMIT 1;");
             cmd.CommandText = sSQL;
                cmd.ExecuteNonQuery();
            }
            if (comboBox1.Text == "Deutsch")
            {

                string sSQL = string.Format("UPDATE sunshine.idlang SET de = 1, eng = 0, ru = 0 LIMIT 1;");
                cmd.CommandText = sSQL;
                cmd.ExecuteNonQuery();
            }
            if (comboBox1.Text == "Русский")
            {

                string sSQL = string.Format("UPDATE sunshine.idlang SET de = 1, eng = 0, ru = 1 LIMIT 1;");
                cmd.CommandText = sSQL;
                cmd.ExecuteNonQuery();
            }
            if (radioButton1.Checked)
            {

                string sSQL = string.Format("UPDATE sunshine.idlang SET idview = 'm';");
                cmd.CommandText = sSQL;
                cmd.ExecuteNonQuery();
            }
            if (radioButton2.Checked)
            {

                string sSQL = string.Format("UPDATE sunshine.idlang SET idview = 's' LIMIT 1;");
                cmd.CommandText = sSQL;
                cmd.ExecuteNonQuery();
            }
           
           

           

         //  cmd.ExecuteNonQuery();
        }

        private void Language_Load(object sender, EventArgs e)
        {
            Exception aException = new Exception();
            string sSQL = string.Format("select idview from idlang");
            try
            {
                lock (_mysqlConnection)
                {
                    if (_mysqlConnection.State != ConnectionState.Open)
                        _mysqlConnection.Open();
                    MySqlDataAdapter ta = new MySqlDataAdapter(sSQL, _mysqlConnection);
                    DataTable dt = new DataTable();
                    ta.Fill(dt);
                    aException = null;
                    if (dt.Rows.Count > 0)
                    {
                        string NN = dt.Rows[0]["idview"].ToString();
                        if (NN == "s")
                        {
                            radioButton1.PerformClick();
                            
                        }
                        if (NN == "m")
                        {
                            radioButton1.PerformClick();
                           
                        }

                    }
                    //return dt;

                }
            }
            catch
            {
                aException = null;
                //return null;
            }
        }
    }
}
