#coding:utf-8
import wx
import numpy as np
import PIL
from PIL import Image 
from wx.lib.embeddedimage import PyEmbeddedImage
import get_data
class About(wx.Frame):
	def __init__(self):
		wx.Frame.__init__(self,None,-1,u'帮助',size=(500,500),style=wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX)
		self.panel=wx.Panel(self)
		string=u'''
		软件开发者：袁秀龙   黄鹏志\n
		软件开发目的：交作业\n
		软件功能：人脸美妆\n
		软件开发时间：2018/06/05\n
		软件开发语言：python && C++ \n
		
		说明: 本次软件开发使用了腾讯开放的免费API,
		在此我们鸣谢腾哥儿及腾讯相关技术团队。
		
		详情请查阅：
		http://ai.qq.com/product/facemakeup.shtml
		'''
		wx.StaticText(self.panel,-1,string,pos=(0,0),size=(500,500),style=wx.ALIGN_LEFT)
	def OnInit(self):
		self.Show()	
class MainWind(wx.Frame):
	def __init__(self):
		self.width = int(1980 );
		self.height = int(1024 );
		self.vertical_pos = 0;
		self.horizontal_pos = 150;
		wx.Frame.__init__(self,None,-1,u'人脸美妆:Developped by Dalong && Bird_Huang',size=(self.width,self.height),style=wx.SYSTEM_MENU|wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX);
		self.bSizer1 = wx.BoxSizer( wx.VERTICAL);
		self.first=0
		self.flag=True
		self.sp=wx.SplitterWindow(self)
		self.p1=wx.Panel(self.sp,style=wx.SUNKEN_BORDER)  
		self.p2=wx.Panel(self.sp,style=wx.SUNKEN_BORDER)  
		self.p1.Hide()  
		self.p2.Hide()
		self.sp1 = wx.SplitterWindow(self.p1) 
		self.bSizer1.Add(self.sp1, 1, wx.EXPAND)
		self.p1.SetSizer(self.bSizer1)
		self.p2.SetBackgroundColour("white")
		self.p1_1 = wx.Panel(self.sp1, style=wx.SUNKEN_BORDER)
		self.p1_2 = wx.Panel(self.sp1, style=wx.SUNKEN_BORDER)
		self.p1_1.Hide()
		self.p1_2.Hide()
		self.p1_1.SetBackgroundColour("white")
		self.p1_2.SetBackgroundColour("white")
		self.sp.SplitHorizontally(self.p2, self.p1, 0)
		self.sp1.SplitVertically(self.p1_1, self.p1_2, 0)
		self.Bind(wx.EVT_ERASE_BACKGROUND, self.OnEraseBackground)
		self.Setbuttons();
		self.input_path = 0;
		self.save_path = 0;
		self.output_image = 0;
		self.input_show = 0;
		self.output_show = 0;
		self.init_button1 = 0;
		self.InitUI();
	def OnInit(self):
		self.Show();
	def InitUI(self):
		
		demo_input =  r"D:\HW2\demo_input.jpg";
		input_image = Image.open(demo_input);
		target_size = (self.width / 2,self.height - self.horizontal_pos - 50);
		input_image = input_image.resize((target_size));
		tmp_path = r"D:\HW2\tmp_input.jpg";
		input_image.save(tmp_path);
		self.pic = wx.Image(tmp_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap();
		self.init_button1 = wx.BitmapButton(self.p1_1, -1, self.pic, pos=(0, 0));
		self.p1_1.Fit();
		demo_input =  r"D:\HW2\demo_output.jpg";
		output_image = Image.open(demo_input);
		output_image = output_image.resize((target_size));
		tmp_path = r"D:\HW2\tmp_output.jpg";
		output_image.save(tmp_path);
		self.pic = wx.Image(tmp_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap();
		self.init_button2 = wx.BitmapButton(self.p1_2, -1, self.pic, pos=(0, 0));
		self.p1_2.Fit();
	def Setbuttons(self):
		Input_Btn=wx.Button(self.p1_1,-1,u'InputImage',pos=(self.width / 2 - 150,(self.height - self.horizontal_pos) - 100),size=(100,50));
		self.Bind(wx.EVT_BUTTON,self.InputImage,Input_Btn);
		self.Bind(wx.EVT_BUTTON,self.InputImage,Input_Btn);
		
		Save_Btn=wx.Button(self.p1_2,-1,u'SaveImage',pos=(self.width / 2 - 150,(self.height - self.horizontal_pos) - 100),size=(100,50));
		self.Bind(wx.EVT_BUTTON,self.SaveImage,Save_Btn);
		Menubar=wx.MenuBar();
		Helpmenu=wx.Menu();
		Helpmenu.Append(1001,u'帮助');
		Aboutmenu=wx.Menu();
		Aboutmenu.Append(1002,u'关于');
		Menubar.Append(Aboutmenu,u'关于');
		Menubar.Append(Helpmenu,u'帮助');
		self.Bind(wx.EVT_MENU,self.Help,id=1001);
		self.Bind(wx.EVT_MENU,self.About,id=1002);
		self.SetMenuBar(Menubar);
		self.Center();
		
	def InputImage(self,event):
		print('dalong log : check input image path');
		dlg = wx.FileDialog(
            self, message="choose a image",
            defaultFile="",
            wildcard='JPGFile(*.jpg)|*.jpg',
            style=wx.FD_OPEN | wx.FD_MULTIPLE | wx.FD_CHANGE_DIR
            );
		if dlg.ShowModal() == wx.ID_OK:
			tmp='';
			paths = dlg.GetPaths();
			for path in paths:
				tmp=tmp+path;
			self.input_path = tmp;
			print('dalong log : check input image path = {}'.format(self.input_path));
			self.Show_InputImage(event);
			self.Show_OutputImage(event);
			return ;
		
	def SaveImage(self,event):
		print('dalong log : check output image path');
		dlg = wx.FileDialog(self, message="save the image ", defaultFile="", wildcard='JPGFile(*.jpg)|*.jpg', style=wx.FD_SAVE);
		if dlg.ShowModal() == wx.ID_OK:
			self.save_path="";
			paths = dlg.GetPaths();
			for path in paths:
				self.save_path = self.save_path + path;
			print('dalong log : check output image path = {}'.format(self.save_path));
			tmp_file = open(self.save_path,'wb');
			if self.output_image == 0:
				file = open(self.input_path, 'rb');
				self.output_image = file.read();
				file.close();
			tmp_file.write(self.output_image);
			tmp_file.close();
	
	def Show_InputImage(self,event):
	
		print('dalong log l: show input image ');
		if not isinstance(self.init_button1,int):
			self.init_button1.Destroy();
			self.init_button2.Destroy();
			self.init_button1 = 1;
		if not isinstance(self.input_show, int):
			self.input_show.Destroy();
			self.input_show = 0;d
		input_image = Image.open(self.input_path);
		target_size = (self.width / 2,self.height - self.horizontal_pos - 50);
		input_image = input_image.resize((target_size));
		tmp_path = r"D:\HW2\tmp_input.jpg";
		input_image.save(tmp_path);
		self.pic = wx.Image(tmp_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap();
		self.input_show = wx.BitmapButton(self.p1_1, -1, self.pic, pos=(0, 0));
		self.p1_1.Fit();
		return 

	def Show_OutputImage(self,event):

		if not isinstance(self.output_show, int):
			self.output_show.Destroy();
			self.output = 0;
		target_size = (self.width / 2,self.height - self.horizontal_pos - 50);
		output_path =  r"D:\HW2\output.jpg";
		print('dalong log : into getData function')
		print('dalong log : check self input path{}'.format(self.input_path));
		ret = get_data.GetData(self.input_path,output_path);
		if ret ==  0:
			output_path = self.input_path;
			print('Beauty Failed');
		output_image = Image.open(output_path);
		
		output_image = output_image.resize((target_size));
		tmp_path = r"D:\HW2\tmp_output.jpg";
		output_image.save(tmp_path);
		self.pic = wx.Image(tmp_path, wx.BITMAP_TYPE_ANY).ConvertToBitmap();
		self.output_show = wx.BitmapButton(self.p1_2, -1, self.pic, pos=(0, 0));
		self.p1_2.Fit();

	def OnEraseBackground(self, evt):
		if self.first<2 or self.flag:
			self.sp.SetSashPosition(self.horizontal_pos);
			self.sp1.SetSashPosition(self.vertical_pos);
			self.p1_1.SetBackgroundColour("white")
			self.p1_2.SetBackgroundColour("white")
			self.first=self.first+1
		self.Refresh()
		return ;
		dc = evt.GetDC();
		if not dc:
			dc = wx.ClientDC(self);
			rect = self.GetUpdateRegion().GetBox();
			dc.SetClippingRect(rect);
		dc.Clear();
		bmp = wx.Bitmap(r"D:\HW2\main.bmp");
		dc.DrawBitmap(bmp, 0, 0);
	def Help(self):
		pass;
	def About(self,event):
		obj=About()
		obj.OnInit()
		
		
if __name__ == "__main__":
	app=wx.App();
	frame=MainWind();
	frame.OnInit();
	app.MainLoop();		
    