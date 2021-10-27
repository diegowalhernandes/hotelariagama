CREATE TABLE IF NOT EXISTS clientes (
ID_cliente smallint auto_increment PRIMARY KEY,
Nome varchar(50) not null,
CPF integer(11),
Telefone integer(10)
);
CREATE TABLE quartos (
ID_quarto char(10),
check_in datetime(6),
check_out datetime(6)
);
CREATE TABLE IF NOT EXISTS reserva (
ID_reserva char(10),
ID_cliente char(10),
ID_quarto char(10),
check_in datetime(6),
check_out datetime(6),
vl_diaria decimal(6),
total_diaria decimal(6)
);

