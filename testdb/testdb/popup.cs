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
    public partial class popup : Form
    {
       

        string _connectionString = "Server=127.0.0.1;Port=3306;Database=sunshine;Uid=root;Pwd=sistem32;Command Timeout=99999; charset = utf8;";
        MySqlConnection _mysqlConnection;
       
        public popup()
        {
           
            InitializeComponent();
        }

        private void popup_Load(object sender, EventArgs e)
        {
            _mysqlConnection = new MySqlConnection(_connectionString);
            Exception aException = new Exception();



            string sQuery = "select * from sunshine.lang order by rand() limit 1";
            string sName;
            string en;
            string de;
            string pl;
            string sp;
            DataTable aTable = GetData(sQuery, out aException);
                label1.Text = "";
              label2.Text = "";
             label3.Text = "";
           label4.Text = "";
          label5.Text = "";

            foreach (DataRow aRow in aTable.Rows)
            {
                sName = aRow["ru"].ToString();
                label1.Text = sName;
            }
            foreach (DataRow aRow in aTable.Rows)
            {
                en = aRow["eng"].ToString();
                label2.Text = en;
            }
            foreach (DataRow aRow in aTable.Rows)
            {
                de = aRow["de"].ToString();
                label3.Text = de;
            }
    /*        foreach (DataRow aRow in aTable.Rows)
            {
                pl = aRow["pl"].ToString();
                label4.Text = pl;
            }
            foreach (DataRow aRow in aTable.Rows)
            {
                sp = aRow["sp"].ToString();
                label5.Text = sp;
            }*/
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

        private void popup_MouseDoubleClick(object sender, MouseEventArgs e)
        {
          
            Form1 f1 = new Form1();
            f1.Visible = true;
            this.Hide();
          
        }
     
    }
}
