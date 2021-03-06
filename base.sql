create database mariogame;
use mariogame;
create table  user(
    id_user varchar(200) primary key not null,
    name_user varchar(200) not null,
    password varchar(200) not null
);
create table player(
    id_player varchar(200) primary key not null, 
    name_player varchar(150) not null
);
create table clan(
    id_clan varchar(200) primary key not null,
    color varchar(100) not null
);

create table user_clan(
    id_clan  varchar(200) not null,
    id_player varchar(200) not null,
    primary key (id_clan,id_player),
    foreign key (id_clan) references clan (id_clan),
    foreign key(id_player) references player(id_player)
);

create table tournament(
    id_tournament varchar(200) primary key not null,
    tournament_name varchar(100),
    type_ int not null
);

alter table tournament add column state int default 0 ;

create table tournament_player(
    id_tournament varchar(200) not null,
    id_player varchar(200) not null,
    primary key(id_tournament,id_player),
    foreign key (id_tournament) references tournament(id_tournament),
    foreign key (id_player) references player(id_player)
);
create table tournament_clans(
    id_tournament varchar(200) not null,
    id_clan varchar(200) not null,
    primary key(id_tournament,id_clan),
    foreign key (id_tournament) references tournament(id_tournament),
    foreign key (id_clan) references clan(id_clan)
);

create table tournament_points_series(
    id_tournament varchar(200) not null,
    id_player varchar(200) not null, 
    foreign key (id_tournament) references tournament(id_tournament),
    foreign key(id_player) references player(id_player),
    primary key (id_tournament,id_player)
);

create table rounds(
    id_round varchar(200) primary key not null,
    id_tournament varchar(200) not null,
    id_player1 varchar(200) not null,
    id_player2 varchar(200) not null,
    id_player3 varchar(200) not null,
    id_player4 varchar(200) not null,
    date_game date,
    round_ int not null,
    group_ int not null,
    points_player1 int ,
    points_player2 int , 
    points_player3 int , 
    points_player4 int , 
    foreign key (id_tournament)
    references tournament(id_tournament),
    foreign key (id_player1) references player(id_player),
    foreign key (id_player2) references player(id_player),
    foreign key (id_player3) references player(id_player),
    foreign key (id_player4) references player(id_player)
);



create table clash_clan
(
    id_clan1 varchar(200) not null,
    id_clan2 varchar(200) not null,
    points_clan1 int not null,
    points_clan2 int not null,
    id_tournament varchar(200),
    primary key(id_clan1,id_clan2,id_tournament),
    foreign key (id_tournament) references tournament(id_tournament),
    foreign key (id_clan1) references clan(id_clan),
    foreign key(id_clan2) references clan(id_clan)
);



SELECT HEX(AES_ENCRYPT("has_key",'password')) as pass;

insert into user values (
UUID(),
'admin',
'BF1E94ECC97F5F918421B9A0E9E3C6F2'
);


insert into clan values
(UUID(),'Green'),
(UUID(),'Yellow'),
(UUID(),'Blue'),
(UUID(),'Pink'),
(UUID(),'Purple'),
(UUID(),'Orange'),
(UUID(),'Red');
