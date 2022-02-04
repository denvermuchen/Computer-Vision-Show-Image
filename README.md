# Computer-Vision-Show-Image
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using Emgu.CV;
using Emgu.CV.Structure;

namespace Emgucv4._4Test //name of project
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)  //type for structure of button 
        {
            try
            {
                string path = @"";  //place where the image's directory
                Image<Bgr, byte> img = new Image<Bgr, byte>(path); //set up the map for colour
                pictureBox1.Image = img.ToBitmap();
            }   
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message); //show image using lib emgucv
            }
        }
    }
}
