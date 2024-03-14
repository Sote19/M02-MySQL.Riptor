CREATE DATABASE Riptor;
USE Riptor;

CREATE TABLE Productos (
id_prod INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
nombre VARCHAR(100) NOT NULL,
precio FLOAT NOT NULL,
color VARCHAR(20) NOT NULL,
marca VARCHAR(30) NOT NULL,
stock INT NOT NULL,
descripcion VARCHAR(100) NOT NULL,
categoria VARCHAR(30) NOT NULL,
materiales VARCHAR(45) NOT NULL
);

CREATE TABLE Usuarios (
id_usu INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
nombre_usu VARCHAR(30) NOT NULL,
apellidos_usu VARCHAR(45) NOT NULL,
pais_usu VARCHAR(30) NOT NULL,
ciudad_usu VARCHAR(30) NOT NULL,
cp_usu INT NOT NULL,
direccion_usu VARCHAR(50) NOT NULL,
telf_usu INT(12) NOT NULL,
correo_usu VARCHAR(30) NOT NULL,
fechanac_usu DATE NOT NULL,
estilo_usu VARCHAR(45) NOT NULL,
contraseña_usu VARCHAR(50) NOT NULL,
ocupacion_usu VARCHAR(30) NOT NULL
);

CREATE TABLE Ventas (
id_vent INT PRIMARY KEY NOT NULL,
id_usu INT /*FK*/ NOT NULL,
cantidadprod_vent INT NOT NULL,
descuento_vent FLOAT NOT NULL,
preiototal_vent FLOAT NOT NULL
);
ALTER TABLE Ventas ADD CONSTRAINT fk_usu FOREIGN KEY (id_usu) REFERENCES Usuarios(id_usu);

CREATE TABLE Facturacion (
dni_fact VARCHAR(9) PRIMARY KEY NOT NULL,
metodo_pago_fact VARCHAR(20) NOT NULL,
direccion_fact VARCHAR (50) NOT NULL,
empresa_fact TINYINT(1) NOT NULL,
fecha_fact DATETIME NOT NULL,
impuestos_fact FLOAT NOT NULL,
precio_total_fact FLOAT NOT NULL,
id_vent INT /*FK*/ NOT NULL
);
ALTER TABLE Facturacion ADD CONSTRAINT fk_vent_1 FOREIGN KEY (id_vent) REFERENCES Ventas(id_vent);

CREATE TABLE Devolucion (
id_dev INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
fecha_dev DATETIME NOT NULL,
motivo_dev VARCHAR(50) NOT NULL,
id_prod INT NOT NULL /*FK*/,
id_vent INT NOT NULL /*FK*/
);
ALTER TABLE Devolucion ADD CONSTRAINT fk_producto_9 FOREIGN KEY (id_prod) REFERENCES Productos(id_prod);
ALTER TABLE Devolucion ADD CONSTRAINT fk_vent FOREIGN KEY (id_vent) REFERENCES Ventas(id_vent);

CREATE TABLE Proveedor (
id_prov INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
contacto_prov VARCHAR(45) NOT NULL,
nombre_prov VARCHAR(100) NOT NULL,
telefono_prov INT(12) NOT NULL,
direccion_prov VARCHAR(100) NOT NULL,
electronico_prov VARCHAR(100) NOT NULL,
id_prod INT NOT NULL /*FK*/
);
ALTER TABLE Proveedor ADD CONSTRAINT fk_producto_7 FOREIGN KEY (id_prod) REFERENCES Productos(id_prod);

CREATE TABLE Categorias (
id_cat INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
nombre_cat VARCHAR(45),
descripcion_cat VARCHAR(100)
);

CREATE TABLE Subcategorias (
id_subcat INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
nombre_subcat VARCHAR(45),
descripcion_subcat VARCHAR(100)
);

CREATE TABLE Sudaderas (
id_suda INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
talla_suda VARCHAR(5) NOT NULL,
capucha_suda TINYINT(1) NOT NULL,
tipobolsillo_suda VARCHAR(30) NOT NULL,
corte_suda VARCHAR(30) NOT NULL,
id_prod INT /*FK*/ NOT NULL 
);
ALTER TABLE Sudaderas ADD CONSTRAINT fk_producto_6 FOREIGN KEY (id_prod) REFERENCES Productos(id_prod);

CREATE TABLE Pantalones (
id_pant INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
talla_pant VARCHAR(10) NOT NULL,
cierre_pant VARCHAR(30) NOT NULL,
corte_pant VARCHAR(30) NOT NULL,
bolsillos_pant INT(10) NOT NULL,
id_prod INT NOT NULL /*FK*/
);
ALTER TABLE Pantalones ADD CONSTRAINT fk_producto_5 FOREIGN KEY (id_prod) REFERENCES Productos(id_prod);

CREATE TABLE Chaquetas (
id_chaq INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
talla_chaq INT(10) NOT NULL,
capucha_chaq TINYINT(1) NOT NULL,
corte_chaq VARCHAR(30) NOT NULL,
id_prod INT NOT NULL /*FK*/
);
ALTER TABLE Chaquetas ADD CONSTRAINT fk_producto_4 FOREIGN KEY (id_prod) REFERENCES Productos(id_prod);

CREATE TABLE Camisetas (
id_cami INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
talla_cami VARCHAR(10) NOT NULL,
corte_cami VARCHAR(30) NOT NULL,
id_prod INT NOT NULL /*FK*/
);
ALTER TABLE Camisetas ADD CONSTRAINT fk_producto_3 FOREIGN KEY (id_prod) REFERENCES Productos(id_prod);

CREATE TABLE Ropa_interior (
id_inter INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
talla_lenceria_inter VARCHAR(45) NOT NULL,
conjunto_inter TINYINT(1) NOT NULL,
id_prod INT NOT NULL /*FK*/
);
ALTER TABLE Ropa_interior ADD CONSTRAINT fk_producto_2 FOREIGN KEY (id_prod) REFERENCES Productos(id_prod);

CREATE TABLE Zapatillas (
id_zapa INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
tallaje_zapa FLOAT NOT NULL,
material_suela_zapa VARCHAR(30) NOT NULL,
id_prod INT NOT NULL /*FK*/
);
ALTER TABLE Zapatillas ADD CONSTRAINT fk_producto_1 FOREIGN KEY (id_prod) REFERENCES Productos(id_prod);

CREATE TABLE Gorras_Gorros (
id_gorr INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
talla_gorr FLOAT NOT NULL,
visera_gorr TINYINT(1) NOT NULL,
cierre_gorr VARCHAR(15) NOT NULL,
id_prod INT NOT NULL /*FK*/
);
ALTER TABLE Gorras_Gorros ADD CONSTRAINT fk_producto FOREIGN KEY (id_prod) REFERENCES Productos(id_prod);

CREATE TABLE Vent_Prod(
id_prod INT,
id_vent INT,
cantidad INT,
PRIMARY KEY(id_prod, id_vent),
FOREIGN KEY (id_prod) REFERENCES Productos(id_prod),
FOREIGN KEY (id_vent) REFERENCES Ventas(id_vent)
);

CREATE TABLE Prod_Sub(
id_prod INT,
id_subcat INT,
PRIMARY KEY(id_prod, id_subcat),
FOREIGN KEY (id_prod) REFERENCES Productos(id_prod),
FOREIGN KEY (id_subcat) REFERENCES Subcategorias(id_subcat)
);

CREATE TABLE Cat_Subcat(
id_cat INT,
id_subcat INT,
PRIMARY KEY(id_cat, id_subcat),
FOREIGN KEY (id_cat) REFERENCES Categorias(id_cat),
FOREIGN KEY (id_subcat) REFERENCES Subcategorias(id_subcat)
);

/*-----------------------INICIO TRIGGERS-------------------------------*/
/*PROCEDURE*/
DELIMITER //
CREATE PROCEDURE Revoke_Privileges(IN usuario VARCHAR(255))
BEGIN
	SET @sql = CONCAT ('REVOKE ALL PRIVILEGES, GRANT OPTION FROM ', usuario);
    PREPARE almac FROM @sql;
    EXECUTE almac;
    DEALLOCATE PREPARE almac;
    END //
/*El procedure se puede usar en cualquier trigger, es como una funcion*/
/*TRIGGER*/    
    CREATE TRIGGER trig_Adios_privilegios
    BEFORE DELETE ON Productos
    FOR EACH ROW
    BEGIN    
		CALL Revoke_Privileges(CURRENT_USER());
	END
// DELIMITER ;

/*TRIGGER*/
USE Riptor;
DELIMITER // 
CREATE TRIGGER trig_actualizar_stock
AFTER INSERT ON Vent_Prod
FOR EACH ROW
BEGIN
    UPDATE Productos
    SET stock = stock - NEW.cantidad
    WHERE id_prod = NEW.id_prod;
END;
// DELIMITER ;

/*TRIGGER*/
USE Riptor;
DELIMITER // 
CREATE TRIGGER trig_mensaje_devolucion
AFTER INSERT ON Devolucion
FOR EACH ROW
BEGIN
    SIGNAL SQLSTATE '54000' SET MESSAGE_TEXT = 'La devolución ha sido registrada correctamente';
END;
// DELIMITER ;
/*-----------------------FIN TRIGGERS-------------------------------*/

/*-----------------------INICIO INDEX'S-------------------------------*/
CREATE INDEX idx_Agil_core ON Productos(id_prod, Stock); /*Hemos pensado que era el mas basico, ya que agiliza la primary key del core también en stock, cuando el usuario compra, para saber si hay stock de x articulo, pensamos que es una busqueda que se realiza muchas veces*/
CREATE INDEX idx_Mejora_relacion ON Vent_Prod (id_prod, id_vent); /*Mejora todo el trafico entre ventas y productos*/
CREATE INDEX idx_categorias ON Categorias (nombre_cat); /*Para busquedas mas rapidas, entre productos y categorias*/
/*-----------------------FIN INDEX'S-------------------------------*/

/*500 REGISTROS PARA LA TABLA "USUARIOS"*/
