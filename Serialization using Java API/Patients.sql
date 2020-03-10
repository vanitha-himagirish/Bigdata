
/*Creates Patients table*/
Create Table Patients(
     PID int primary key identity(1,1),
     Name varchar(30) Not Null,
     Phone char(10),
     Email varchar(50),
     Username varchar(20),
     Password varchar(20)
    );

/*Inserts records to Patients table*/
Insert into Patients(Name,Phone,Email,Username,Password) values ('Patient1', '913234544' , 'pat@hosp.com','pat1','pat1');
Insert into Patients(Name,Phone,Email,Username,Password) values ('Patient2', '913234545' , 'pat2@hosp.com','pat2','pat2');
Insert into Patients(Name,Phone,Email,Username,Password) values ('Patient3', '913234546' , 'pat3@hosp.com','pat3','pat3');
Insert into Patients(Name,Phone,Email,Username,Password) values ('Patient4', '913234547' , 'pat4@hosp.com','pat4','pat4');
Insert into Patients(Name,Phone,Email,Username,Password) values ('Patient5', '913234548' , 'pat5@hosp.com','pat5','pat5');

/*Selects records from Pateints*/
select * from Patients