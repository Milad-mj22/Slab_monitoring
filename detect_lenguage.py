from PyQt5.QtGui import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from pyqt5_plugins import *
import sqlite3
from sqlite3 import Error

from PySide6.QtCore import *

from PySide6.QtWidgets import *
def language():
    conn = sqlite3.connect('settings.db')
    cur = conn.cursor()       
    cur.execute('select * from language')
    rec = cur.fetchall()
    conn.commit()
    conn.close()    
    return str(rec[0][0])

def main_window(self):
    
    self.label_3.setText('نرم افزار مانیتورینگ اسلب')
    
    # self.label_6.setText('دوربین های در دسترس')
    self.groupBox.setTitle('جزئیات اسلب')
    self.groupBox_2.setTitle('افزودن عیب')
    self.label_2.setText('لیست عیوب')
    self.automatic_btn.setText('اتوماتیک')
    self.manual_btn.setText('دستی')
    self.start_capture.setText('شروع تصویر برداری')
    self.stop_capture.setText('پایان تصویر برداری')
    
    self.label_26.setText('سرعت خط')
    self.label_2.setText('لیست عیوب')
    self.label_28.setText('ایدی اسلب')
    self.label_31.setText('شماره خط')
    self.label_50.setText('عرض')
    self.label_57.setText('طول')
    self.label_52.setText('پهنا')
    self.label_51.setText('وزن')
    self.label_35.setText('شماره ذوب')
    
    #self.test_btn.setText('بروزرسانی')
    # self.label_time.setText('ساعت')
    # self.save_btn.setText('ذخیره سازی')
    self.label_59.setText('سرعت پردازش')
    # self.start_btn.setText('اتصال')
    self.live_btn.setText('  صفحه اول')
    self.page_live_dataset_btn.setText('  صفحه دوم')
    self.panorama_btn.setText('  پانوراما')
    self.page_fullscreen.setText('  تمام صفحه')

    self.page_report_btn.setText('  گزارش گیری')
    self.page_aboutus_btn.setText('  ارتباط با ما')
    self.logout_btn.setText('خروج از حساب   کاربری')
    # self.start_btn_live.setText('اتصال')
    # self.label_22.setText('سرعت خط')
    # self.label_35.setText('ایدی اسلب')
    # self.label_37.setText('پهنا')

    self.export_btn.setText('خروجی اکسل')
    # self.label_21.setText('اخرین خطوط')
    # self.request_btn.setText('درخواست')
    # self.search_id_btn.setText('جست و جو')

    self.label_29.setText(': جستجو در آخرین موارد')
    self.label_37.setText(': جستجو با شماره آیدی')
    self.label_30.setText(': جستجو با شماره خط')
    self.label_47.setText(': جستجو با تاریخ')
    self.label_53.setText(': جستجو با ساعت')
    self.label_71.setText(': جستجو با عرض')
    self.label_74.setText(': جستجو با وزن')
    self.label_48.setText('تاریخ شروع :')
    self.label_56.setText('تاریخ پایان :')
    self.label_54.setText('ساعت شروع :')
    self.label_55.setText('ساعت پایان :')

    self.label_72.setText(' کمینه :')
    self.label_73.setText('  بیشینه :')

    self.label_75.setText(' کمینه :')
    self.label_76.setText('  بیشینه :')
    # self.search_line_btn.setText('جست و جو')
    # self.label_54.setText('تاریخ شروع')
    # self.label_55.setText('تاریخ پایان')
    # self.search_date.setText('جست و جو')
    # self.search_id_btn_4.setText('جست و جو')
    # self.search_width.setText('جست و جو')
    # self.search_weight.setText('جست و جو')
    self.full_search.setText('جست و جو')
   
    self.label_33.setText('اموزش نرم افزار')
    self.backup_btn.setText('بکاپ گیری')
    self.btn_now_time.setText('ساعت حال')
    self.clear_checkboxes_btn.setText('پاک کردن تیک های جدول')
    self.edit_btn.setText('تغییر مقدار')
    self.checkBox_top.setText('دوربین پیشانی')
    self.checkBox_head.setText('دوربین بالا')
    self.checkBox_mesh.setText('مش')
    self.checkBox_mesh.setText('مش')
    self.label_13.setText('اتصال')
    self.label_14.setText('قطع اتصال')
    self.label_15.setText('به روزرسانی')
    self.label_16.setText('کالیبراسیون')
    # self.label_38.setText('فریم بر ثانیه')
    
    






def login_window(self):
    self.lineEdit.setPlaceholderText('نام کاربری')
    self.lineEdit_2.setPlaceholderText('رمز عبور')
    self.login_btn.setText('ورود')
    self.close_btn.setText('خروج')
    #self.lineEdit.setText('نام کاربری')

def setting_window(self):
    self.software_settings.setText('تنظیمات نرم افزار')
    self.camera_settings.setText('تنظیمات دوربین')
    self.manage_user_btn.setText('مدیریت کاربران')
    self.pop_settings.setText('تنظیمات ارتباطی')
    self.report_settings.setText('تنظیمات گزارش گیری')
    self.calibration_settings.setText('تنظیمات کالیبراسیون')
    self.close_btn.setText('')
    self.close_btn.setText('')

def default_setting(self):
    self.label_21.setText('    تنظیمات نرم افزار')
    self.label_22.setText('    صفحه پخش زنده')
    self.label_23.setText('                                                                         دوربین 1')
    self.label_24.setText('                                                                        دوربین 2')
    self.label_25.setText('                                                                        دوربین 3')
    self.label_26.setText('                                                                        دوربین 4')
    self.label_31.setText('     صفحه پخش زنده دیتاست')
    self.close_btn.setText('')
    self.close_btn.setText('خروج')
    self.label_27.setText('                                                                         دوربین 1')
    self.label_28.setText('                                                                        دوربین 2')
    self.label_29.setText('                                                                        دوربین 3')
    self.label_30.setText('                                                                        دوربین 4')
    self.label_41.setText('     نام دوربین ها')
    self.label_36.setText('                                                                         دوربین 1')
    self.label_37.setText('                                                                        دوربین 2')
    self.label_38.setText('                                                                        دوربین 3')
    self.label_39.setText('                                                                        دوربین 4')
    self.label_40.setText('                                                             زبان')
    self.label_35.setText('                                                         تنظیم استایل')
    self.label_34.setText('      تاییدیه برای ذخیره سازی:')
    self.radioButton_4.setText('فعالسازی')
    self.radioButton_3.setText('غیر فعالسازی')
    #self.label_32.setText('                                                                                                      : تعیین صفحه پیش فرض')
    self.label_32.setText('   تعیین صفحه پیش فرض :')
    self.radioButton_2.setText('صفحه پخش زنده دیتاست')
    self.radioButton.setText('صفحه پخش زنده')
    self.label_33.setText('   لیست عیوب')
    self.save_btn.setText('ذخیره')
    self.save_close_btn.setText('ذخیره')
    self.help_btn.setText('راهنمایی')

    self.radioButton_2.setGeometry(37, 433, 131, 16)
    self.radioButton.setGeometry(160, 433, 131, 16)

def camera_setting(self):
    self.label_21.setText('تنظیمات دوربین')
    self.label_15.setText('  دوربین 1')
    self.label.setText('  نام دوربین:      ')
    # self.comboBox_1.setGeometry(40,25,241,22)
    self.comboBox_1.setLayoutDirection(Qt.RightToLeft)
    self.label_2.setText('   گین:')
    self.label_3.setText('   شدت روشنایی:')
    self.label_4.setText('   پهنای باند:')
    self.line_gain_cam_1.setText('')
    self.line_exposure_cam_1.setText('')
    self.line_bandwight_cam_1.setText('')
    self.line_gain_cam_1.setGeometry(40,65,201,22)
    self.line_exposure_cam_1.setGeometry(40,105,201,22)
    self.line_bandwight_cam_1.setGeometry(40,145,201,22)

    self.label_16.setText('  دوربین 2')
    self.label_8.setText('  نام دوربین:      ')
    # self.comboBox_2.setGeometry(50,25,241,22)
    self.comboBox_2.setLayoutDirection(Qt.RightToLeft)
    self.label_6.setText('   گین:')
    self.label_7.setText('   شدت روشنایی:')
    self.label_5.setText('   پهنای باند:')
    self.line_gain_cam_2.setText('')
    self.line_exposure_cam_2.setText('')
    self.line_bandwight_cam_2.setText('')
    self.line_gain_cam_2.setGeometry(50,65,201,22)
    self.line_exposure_cam_2.setGeometry(50,105,201,22)
    self.line_bandwight_cam_2.setGeometry(50,145,201,22)

    self.label_17.setText('  دوربین 3')
    self.label_20.setText('  نام دوربین:      ')
    # self.comboBox_3.setGeometry(40,33,241,22)
    self.comboBox_3.setLayoutDirection(Qt.RightToLeft)
    self.label_14.setText('   گین:')
    self.label_19.setText('   شدت روشنایی:')
    self.label_13.setText('   پهنای باند:')
    self.line_gain_cam_3.setText('')
    self.line_exposure_cam_3.setText('')
    self.line_bandwight_cam_3.setText('')
    self.line_gain_cam_3.setGeometry(40,73,201,22)
    self.line_exposure_cam_3.setGeometry(40,113,201,22)
    self.line_bandwight_cam_3.setGeometry(40,154,201,22)

    self.label_18.setText('  دوربین 4')
    self.label_10.setText('  نام دوربین:      ')
    # self.comboBox_4.setGeometry(50,33,241,22)
    self.comboBox_4.setLayoutDirection(Qt.RightToLeft)
    self.label_12.setText('   گین:')
    self.label_11.setText('   شدت روشنایی:')
    self.label_9.setText('   پهنای باند:')
    self.line_gain_cam_4.setText('')
    self.line_exposure_cam_4.setText('')
    self.line_bandwight_cam_4.setText('')
    self.line_gain_cam_4.setGeometry(50,73,201,22)
    self.line_exposure_cam_4.setGeometry(50,113,201,22)
    self.line_bandwight_cam_4.setGeometry(50,154,201,22)
    

    self.label_25.setText('')



    self.save_close_btn.setText('ذخیره')
    self.help_btn.setText('راهنمایی')
    self.close_btn.setText('خروج')
    self.label_22.setText(' دوربین پیش فرض برای تشخیص اشبا:')

    # self.close_btn.setText('')

def confirm_window(self):
    self.yes_btn.setText('    بله')
    self.no_btn.setText('     خیر')