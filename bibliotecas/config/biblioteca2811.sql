create database biblioteca;
use biblioteca;

create table if not exists usuario(
	id_usuario int primary key auto_increment,
    nome varchar(100),
    email varchar(30),
    cpf varchar(13),
    senha varchar(15),
    administrador boolean default false
);

create table if not exists livro(
 id_livro int auto_increment primary key,
 titulo varchar(255),
 autor varchar(255),
 isbn varcahr(13) unique not null,
 genero varchar(50),
 status varchar(255) default 'disponível'
);

create table if not exists emprestimo(
	id_emprestimo int auto_increment primary key,
    id_livro int not null,
    id_usuario int not null,
    data_emprestimo date default current_date,
    data_devolução date,
    foreign key (id_livro) references livro(id_livro),
	foreign key (id_usuario) references usuario(id_usuario)
);