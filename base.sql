create database mariogame;
use mariogame;
create table  user(
    id_user binary(16) primary key not null,
    name_user varchar(200) not null,
    password varchar(200) not null
);
create table player(
    id_player binary(16) primary key not null, 
    name_player varchar(150) not null
);
create table clan(
    id_clan binary(16) primary key not null,
    color varchar(100) not null
);

create table user_clan(
    id_clan binary(16) not null,
    id_player binary(16) not null,
    primary key (id_clan,id_player),
    foreign key (id_clan) references clan (id_clan),
    foreign key(id_player) references player(id_player)
);

create table tournament(
    id_tournament binary(16) primary key not null,
    tournament_name varchar(100),
    date_start date not null,
    date_finish date not null
);
create table states(
    id_state binary(16) primary key not null,
    state varchar(30) not null
);

create table tournament_player(
    id_tournament binary(16) not null,
    id_player binary(16) not null,
    state binary(16) not null,
    primary key(id_tournament,id_player),
    foreign key(state) references states(id_state),
    foreign key (id_tournament) references tournament(id_tournament),
    foreign key (id_player) references player(id_player)
);

create table rounds(
    id_round binary(16) primary key not null,
    id_tournament binary(16) not null,
    id_player1 binary(16) not null,
    id_player2 binary(16) not null,
    id_player3 binary(16) not null,
    id_player4 binary(16) not null,
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
    id_clash binary(16) primary key not null,
    id_clan1 binary(16) not null,
    id_clan2 binary(16) not null,
    date_ date not null,
    points_clan1 int not null,
    points_clan2 int not null,
    rounds int not null,
    id_tournament binary(16),
    foreign key (id_tournament) references tournament(id_tournament),
    foreign key (id_clan1) references clan(id_clan),
    foreign key(id_clan2) references clan(id_clan)
);


