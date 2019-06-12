using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
using MySql.Data.MySqlClient;
using System.Data;

namespace testdb
{
    static class Program
    {
        /// <summary>
        /// Главная точка входа для приложения.
        /// </summary>
        [STAThread]
        static void Main()
        {
            string _connectionString = "Server=127.0.0.1;Port=3306;Database=sunshine;Uid=root;Pwd=sistem32;Command Timeout=99999";
            MySqlConnection _mysqlConnection;
             _mysqlConnection = new MySqlConnection(_connectionString);
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
                     if (dt.Rows.Count>0)
                     {
                         string NN = dt.Rows[0]["idview"].ToString();
                         if (NN == "s")
                         {
                             Application.EnableVisualStyles();
                             Application.SetCompatibleTextRenderingDefault(false);
                             Application.Run(new popup()); 
                         }
                         if (NN == "m")
                         {
                             Application.EnableVisualStyles();
                             Application.SetCompatibleTextRenderingDefault(false);
                             Application.Run(new Form1());
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
