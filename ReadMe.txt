<본 프로젝트 케이싱 규칙>
-폴더명, 클래스, 함수 : 파스칼 케이싱
-변수, 매개변수 : 카멜케이싱


<데이터베이스 프로시저>
//테이블 데이터를 전부 삭제하는 프로시저
CREATE PROCEDURE `del` ()
BEGIN
delete from findlost.main_lostitemstemp;
alter table findlost.main_lostitemstemp auto_increment=0;
END

//테이블을 교체하는 프로시저
CREATE PROCEDURE `changeTable` ()
BEGIN
 RENAME TABLE findlost.main_lostitems TO temp;
 RENAME TABLE findlost.main_lostitemstemp TO findlost.main_lostitems;
 RENAME TABLE temp TO findlost.main_lostitemstemp;
END


