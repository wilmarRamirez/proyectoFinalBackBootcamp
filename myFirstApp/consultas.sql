-- tabla best--------------------
INSERT INTO public."myApp_best"(
	 ciudad_pais, dia_prueba, valor)
	VALUES ('Rome, Italty' , 10, '5,42k');
	
INSERT INTO public."myApp_best"(
	 ciudad_pais, dia_prueba, valor)
	VALUES ('London, Uk' , 7, '2,42k');
	
INSERT INTO public."myApp_best"(
	 ciudad_pais, dia_prueba, valor)
	VALUES ('Osaka, Japan' , 10, '5,42k');
	
--tabla exclusive-----------------

INSERT INTO public."myApp_exclusive"(
	 ciudad, pais, valor_anterior, valor_actualizado)
	VALUES ('Madrid' , 'Spain', '950', '850');
	
INSERT INTO public."myApp_exclusive"(
	 ciudad, pais, valor_anterior, valor_actualizado)
	VALUES ('Firenze' , 'Italy', '850', '750');
	
INSERT INTO public."myApp_exclusive"(
	 ciudad, pais, valor_anterior, valor_actualizado)
	VALUES ('paris' , 'france', '699', '599');
	
INSERT INTO public."myApp_exclusive"(
	 ciudad, pais, valor_anterior, valor_actualizado)
	VALUES ('London' , 'Uk', '950', '850');
	
---tabla lastestblog---------------

INSERT INTO public."myApp_latestblog"(
	 title, fecha)
	VALUES ('Travel far enough, you meet yourself' , 'July 27, 2021');
	
INSERT INTO public."myApp_latestblog"(
	 title, fecha)
	VALUES ('How to Save Money While Visiting Africa' , 'July 27, 2021');
	
INSERT INTO public."myApp_latestblog"(
	 title, fecha)
	VALUES ('Reflections on 5 Months of Travel: Time to Hang' , 'July 27, 2021');
	
INSERT INTO public."myApp_latestblog"(
	 title, fecha)
	VALUES ('The Amazing Difference a Year of Travelling' , 'July 27, 2021');

select * from "myApp_latestblog";

select * from "myApp_exclusive";

select * from "myApp_best";

