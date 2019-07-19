<본 프로젝트 케이싱 규칙>
-폴더명, 클래스, 함수 : 파스칼 케이싱
-변수, 매개변수 : 카멜케이싱



<데이터베이스 프로시저>
CREATE PROCEDURE `del` ()
BEGIN
delete from findlost.main_lostitems;
alter table findlost.main_lostitems auto_increment=0;
END

//프로시저를 사용하는 이유 .. 그냥 코드수 줄고 깔끔해서.. 딱히 그럴싸한 이유가 없음 사실