create database biblioteca;
use biblioteca;

create table usuario(
	id_usuario int primary key auto_increment,
    nome varchar(100),
    cpf varchar(13),
    telefone varchar(20)
);


create table livro (
 id_livro int auto_increment primary key,
 titulo varchar(50),
 autor varchar(50),
 genero varchar(50),
 status varchar(30),
 codigo int
);

create table emprestimo(
	id_emprestimo int auto_increment primary key,
    id_livro int,
    id_usuario int,
     foreign key (id_livro) references livro(id_livro),
	 foreign key (id_usuario) references usuario(id_usuario)

);