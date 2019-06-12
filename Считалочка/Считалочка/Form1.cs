using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using System.Drawing;
using System.Drawing.Imaging;



namespace Считалочка
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private int t2;
        private int x;
        private int y;
        private string t;
        private int p=3;
        private int _minus;
        private int ball;
        Button bt = new Button();
        Button btn = new Button();
        Button btnp = new Button();
        Label lb1 = new Label();
        Label lb2 = new Label();
        Label lb3 = new Label();
        Label lb4 = new Label();
        Label lb5 = new Label();
        Label lb6 = new Label();
        TextBox tb = new TextBox();
        TextBox tb1 = new TextBox();
        PictureBox img1 = new PictureBox();
        PictureBox img2 = new PictureBox();
        PictureBox img3 = new PictureBox();
        private void Form1_Load(object sender, EventArgs e)
        {
            Random minus = new Random();
            _minus = minus.Next(1, 3);
            Random rndx = new Random();
            x = rndx.Next(1, 13);
            Random rndy = new Random();
            y = rndy.Next(0, 13);
            if (y == 0)
            {
                y = y + 1;
            }
                ///BUTTONS
            ///
            
            bt.Name = "Button1";
            bt.Size = new Size(75, 25);
            bt.Location = new Point(450, 250);
            bt.Text = "Проверить";
            this.Controls.Add(bt);
            bt.Click += new System.EventHandler(this.bt_Click);
            bt.Font = new Font("Arial",8);

            btn.Name = "Button2";
            btn.Size = new Size(75, 25);
            btn.Location = new Point(450, 285);
            btn.Text = "Закрыть";
            this.Controls.Add(btn);
            btn.Click += new System.EventHandler(this.btn_Click);
            btn.Font = new Font("Arial", 8);

            btnp.Name = "Button3";
            btnp.Size = new Size(75, 25);
            btnp.Location = new Point(450, 85);
            btnp.Text = "Подсказка";
            this.Controls.Add(btnp);
            btnp.Click += new System.EventHandler(this.btnp_Click);
            btnp.Font = new Font("Arial", 8);

            
            ///LABELS
            ///
              
               lb1.Name = "label1";
               lb1.Size = new Size(45, 35);
               lb1.Location = new Point(50, 125);
               lb1.Text = x.ToString();
               this.Controls.Add(lb1);
    //           string z = lb1.Text;
               lb1.Font = new Font("Arial", 18);
               lb1.TextAlign = ContentAlignment.BottomCenter;

            
               lb2.Name = "label2";
               lb2.Size = new Size(45, 35);
               lb2.Location = new Point(125, 125);
               this.Controls.Add(lb2);
               lb2.Font = new Font("Arial", 24);
               lb2.TextAlign = ContentAlignment.BottomCenter;
               if (_minus == 1)
               { lb2.Text = ("+"); }
               else
               { lb2.Text = ("-"); }
             
               lb3.Name = "label3";
               lb3.Size = new Size(45, 35);
               lb3.Location = new Point(200, 125);
               lb3.Text = y.ToString();   
               this.Controls.Add(lb3);
             //  string f = lb3.Text;
               lb3.Font = new Font("Arial", 18);
               lb3.TextAlign = ContentAlignment.BottomCenter;
   
               lb4.Name = "label4";
               lb4.Size = new Size(45, 35);
               lb4.Location = new Point(275, 125);
               lb4.Text = ("=");
               this.Controls.Add(lb4);
               lb4.Font = new Font("Arial", 24);
               lb4.TextAlign = ContentAlignment.BottomCenter;

          lb5.Name = "label5";
          lb5.Text = "Попробуй ещё раз";
          lb5.Visible = false;
          lb5.Size = new Size(185, 25);
          lb5.Location = new Point(200, 75);
          this.Controls.Add(lb5);
          lb5.Font = new Font("Arial", 15);
          lb5.TextAlign = ContentAlignment.BottomCenter;

          lb6.Name = "label6";
          lb6.Text = "";
          lb6.Visible = false;
          lb6.Size = new Size(45, 35);
          lb6.Location = new Point(400, 55);
          this.Controls.Add(lb6);
          lb6.Font = new Font("Arial", 15);
          lb6.TextAlign = ContentAlignment.MiddleCenter;

            ///TEXTBOX
          
          tb.Name = "textbox1";
          tb.Size = new Size(75, 65);
          tb.Location = new Point(400, 125);
          this.Controls.Add(tb);
          tb.Font = new Font("Arial", 19);
          tb.TextAlign = HorizontalAlignment.Center;

          tb1.Name = "textbox2";
          tb1.Size = new Size(185, 15);
          tb1.Location = new Point(20, 25);
          this.Controls.Add(tb1);
          tb1.Font = new Font("Arial", 14);
          tb1.Enabled = false;
          tb1.Text = "У тебя" + " " + ball + " " + "балл (а/ов)";

            ///images
          
          img1.Name = "img1";
          img1.Size = new Size(115, 55);
          img1.Location = new Point(50, 250);
          img1.Image = Res.sol;
          img1.SizeMode = PictureBoxSizeMode.StretchImage;
          this.Controls.Add(img1);
          
          img2.Name = "img2";
          img2.Size = new Size(215, 35);
          img2.Location = new Point(100, 350);
          img2.Visible = false;
          this.Controls.Add(img2);

        
          img3.Name = "img3";
          img3.Size = new Size(55, 55);
          img3.Location = new Point(470, 15);
          img3.Image = Res.c3;
          img3.SizeMode = PictureBoxSizeMode.StretchImage;
          this.Controls.Add(img3);
        
        }
        private void btnp_Click(object sender, EventArgs e)
        {
            p = p - 1;
            if (p == 2)
            {
                img3.Image = Res.с2;
            }
            if (p == 1)
            {
                img3.Image = Res.с1;
            }
            if (p == 0)
            {
                img3.Image = Res.с0;
                btnp.Enabled = false;
            }
            if (_minus == 1)
            {
                int pods = x + y;
                lb6.Text = pods.ToString();
            }
            if (_minus != 1)
            {
                int pods = x - y;
                lb6.Text = pods.ToString();
            }
           
            lb6.Visible = true;
        }
        private void btn_Click(object sender, EventArgs e)
        {
            Application.Exit();
        }

        private void bt_Click(object sender, EventArgs e)
        {
            lb6.Visible = false;
       
    try
        {
         
         
         string t =tb.Text;
         int t1 = int.Parse(t);
        if (_minus == 1)
    {
        t2 = x + y;
        lb2.Text = ("+");
    }
        if (_minus == 2)
        {
               t2 = x - y;
            lb2.Text = ("-");
        }
        
         if (t1 == t2)
         {
             img1.Image = Res.ok;
             img1.SizeMode = PictureBoxSizeMode.StretchImage;
             img1.Visible = true;
             img2.Image = Res.um;
             img2.SizeMode = PictureBoxSizeMode.StretchImage;
             img2.Visible = true;
         qwer:
             Random rndx = new Random();
             x = rndx.Next(1, 13);
             Random rndy = new Random();
             y = rndy.Next(0, 13);
             if (y == 0)
             {
                 y = y + 1;
             }
             if (x + y == t2)
             {
                goto qwer;
            
            }
             if (x == y)
             {
                 Random count = new Random();
                 int Ad = count.Next(1, 5);
                 x = x + Ad;
                 int x2 = x;
                 lb1.Text = x2.ToString();
             }
             if(x<y)
             {
                 Random count = new Random();
                 int Ad = count.Next(1, 5);
                 int c=y;
             x = c + Ad;
             }
              lb3.Text = y.ToString();
             lb1.Text = x.ToString();
             lb5.Visible = false;
             tb.Text = "";
             ball = ball + 1;

             tb1.Text = "У тебя" + " " + ball + " " + "балл (а/ов)";
             if (ball ==20)
             {
                 lb5.Visible = true;
                 lb5.Text = "Класс!!";
             }
             if (ball == 40)
             {
                 lb5.Visible = true;
                 lb5.Text = "Молодец!!";
             }
             if (ball == 75)
             {
                 lb5.Visible = true;
                 lb5.Text = "Замечательно!!";
             }
             if (ball == 100)
             {
                 lb5.Visible = true;
                 lb5.Text = "Великолепно!!";
             }
             if (ball == 150)
             {
                 lb5.Visible = true;
                 lb5.Text = "Превосходно!!";
             }
        //    else { lb5.Text = "Попробуй ещё раз"; }
          

          
         }
         if (t1!=t2)
         {
             img1.Image = Res.no;
             img1.SizeMode = PictureBoxSizeMode.StretchImage;
             img1.Visible = true;
             img2.Image = Res.ms;
             img2.SizeMode = PictureBoxSizeMode.StretchImage;
             img2.Visible = true;
             lb5.Visible = true;
             ball = ball - 1;
             if (ball < 0)
             { ball = 0; }
             tb1.Text = "У тебя" + " " + ball + " " + "балл (а/ов)";

         }

            }
    catch (FormatException)
    {
        TextBox tb = new TextBox();
        if (tb.Text == "")
        { MessageBox.Show("Ошибка. Вы не ввели число"); }
      
        }
    Random minus = new Random();
    _minus = minus.Next(1, 3);
    if (_minus == 1)
    {
     //   t2 = x + y;
        lb2.Text = ("+");
    }
    if (_minus == 2)
    {
     //   t2 = x - y;
        lb2.Text = ("-");
    }
    }

    }

}
