# Dormitory_Noise_Control_System

1. clientUi(소켓).py 설명 (수정중)
  - MyTableWidget 클래스: ttk.Treeview를 상속 + 테이블 위젯을 만든다.
  - initUI 메서드: GUI를 초기화 및 소리 수준이 일정 기준을 초과할 경우 경고 횟수 증가
  - cell_was_clicked 메서드 : 테이블 위젯의 셀이 클릭 되었을때 호출
  - buttonClicked 메서드 : 경고 버튼이 클릭 되었을때 호출되는 메서드
