import os
class MonHoc():
    def __init__(self,MaMH,TenMH,SoTC):
        self.MaMH=MaMH
        self.TenMH=TenMH
        self.SoTC=SoTC
    def HienThi(self):
        print("Mã Môn Học là ",self.MaMH)
        print("Tên Môn Học Là ",self.TenMH)
        print("Số Tín Chỉ Là ",self.SoTC)
dsMH=[]
def Show():
    os.system('cls')
    print("-------------------------")
    print('Menu Lựa Chọn:')
    print('1.Thêm Môn Học')
    print("2.Hiện Thị Các Môn Học")
    print('3.Xóa Môn Học')
    print("4.Tìm Kiếm Môn Học")
    print("5.Cập Nhật Môn Học ")
    print("0.Thoát Khỏi Chương Trình")
def Nhap():
    n=int(input("Nhập Số Lượng Môn Học :"))
    for i in range(n):
        MaMH=input("Nhập Mã Môn Học ")
        TenMH=input("Nhập Tên Môn Học ")
        SoTC=input("Nhập số tín chỉ ")
        mh=MonHoc(MaMH,TenMH,SoTC)
        dsMH.append(mh)
def hienthi():
    if dsMH!=[]:
        for i in range(len(dsMH)):
            print("Thông tin môn học thứ ", i+1)
            dsMH[i].HienThi()
    else:
        print("Không Có Môn Học Để Hiện Thị")
        print("Mời Bạn Nhập Lại ")
def themMH():
    k=int(input("Nhập số môn học cần thêm "))
    for i in range(k):
        MaMH=input("Nhập Mã Môn Học ")
        TenMH=input("Nhập Tên Môn Học ")
        SoTC=input("Nhập số tín chỉ ")
        mh=MonHoc(MaMH,TenMH,SoTC)
        dsMH.append(mh)
def xoaMh(Maxoa):
    for mh in dsMH:
        if(mh.MaMH==Maxoa):
            dsMH.remove(mh)
            print(f"Đã Xóa Được Môn Học {mh.TenMH} ")
        else :
            print("Mã Môn Học Bạn Vừa Nhập Không Có ")
            print("Mời Bạn Chọn Lại")    

def PhuongThucTimKiem():
    while True:
        Method_Search=input("Nhập Phương Thức Cần Tìm Kiếm(Ma || Ten || TinChi) hoặc kết thúc (OUT) ")
        if Method_Search.upper()=='MA':
            for i in range(len(dsMH)):
                while True:
                    h=input("Nhập Mã Môn Học Cần Tìm Kiếm  ")
                    if h !=dsMH[i].MaMH:
                        print('Không có mã môn học này trong chương trình.Mời Bạn Nhập Lại')
                        k=input("Chọn Y để nhập lại hoặc chọn O để chọn lại phương thức tìm kiếm ")
                        if k.upper()=="Y":
                            pass
                        if k.upper()=="O":
                            break
                    else:
                        dsMH[i].HienThi()
                        break
        if Method_Search.upper()=='TEN':
            for i in range(len(dsMH)):
                while True:
                    h=input("Nhập Tên Môn Học Cần Tìm Kiếm  ")
                    if h !=dsMH[i].TenMH:
                        print('Không có Tên môn học này trong chương trình.Mời Bạn Nhập Lại')
                        k=input("Chọn Y để nhập lại hoặc chọn O để chọn lại phương thức tìm kiếm ")
                        if k.upper()=="Y":
                            pass
                        if k.upper()=="O":
                            break
                    else:
                        dsMH[i].HienThi()
                        break
        if Method_Search.upper()=='TINCHI':
            for i in range(len(dsMH)):
                while True:
                    h=input("Nhập Tín Chỉ Môn Học Cần Tìm Kiếm  ")
                    if h !=dsMH[i].MaMH:
                        print('Không có Tín Chỉ môn học này trong chương trình.Mời Bạn Nhập Lại')
                        k=input("Chọn Y để nhập lại hoặc chọn O để chọn lại phương thức tìm kiếm ")
                        if k.upper()=="Y":
                            pass
                        if k.upper()=="O":
                            break
                    else:
                        dsMH[i].HienThi()
                        break
        if Method_Search.upper()=='OUT':
            break
def CapNhatMonHoc(MaUpdate):
    for mh in dsMH:
        if (mh.TenMH)==MaUpdate:
            while True:
                newName=input("Nhập Tên Mới Của Môn Học ")
                
                if mh.TenMH==newName or newName == "":
                    print("Tên Đã Trùng Với Tên Một Môn Học Khác Hoặc Bạn Chưa Ghi.Mời Nhập Lại ")
                else:
                    break
            while True :
                newMaMH=input('Nhập Mã Mới Của Môn Học ')
                if mh.MaMH==newMaMH or newMaMH == "":
                    print("Mã Môn Học Đã Trùng Với Mã Môn Học Một Môn Học Khác.Mời Nhập Lại  ")
                else:
                    break
            newTC=input('Nhập Tín Chỉ Mới Của Môn Học ')    
            mh.SoTC=newTC
            mh.TenMH=newName
            mh.MaMH=newMaMH
        else:
            print('Môn Bạn Vừa Nhập Không Có Trong Bảng ')
def main():
    Show()
    while True:
        key=int(input("Nhập mục cần chọn: "))
        match key:
            case 1:
                Nhap()
            case 2:
                print('Bảng Thông Báo Thông Tin Các Môn Học :')
                hienthi()
            case 3:
                z=input('Nhập Mã Môn Học Cần Xóa ') 
                xoaMh(z)
            case 4:
                PhuongThucTimKiem()
            case 5:
                m=input("Nhập Tên Môn Học Cần Cập Nhật ")
                CapNhatMonHoc(m)
            case 0:
                print("Bạn Đã Thoát Chương Trình.GoodBye")
                quit()
            case 9:
                print("Bạn Chọn Sai")
main()
