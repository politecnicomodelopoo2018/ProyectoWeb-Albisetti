-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema web
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema web
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `web` DEFAULT CHARACTER SET utf8 ;
USE `web` ;

-- -----------------------------------------------------
-- Table `web`.`categoria_evento`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `web`.`categoria_evento` (
  `idCategoria` INT NOT NULL AUTO_INCREMENT,
  `cat_evento` VARCHAR(50) NULL,
  `icono` VARCHAR(15) NULL,
  PRIMARY KEY (`idCategoria`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `web`.`invitados`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `web`.`invitados` (
  `idInvitado` INT NOT NULL AUTO_INCREMENT,
  `nombre_invitado` VARCHAR(45) NULL,
  `apellido_invitado` VARCHAR(45) NULL,
  `descripcion` VARCHAR(45) NULL,
  `url_imagen` VARCHAR(50) NULL,
  PRIMARY KEY (`idInvitado`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `web`.`eventos`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `web`.`eventos` (
  `idEvento` INT NOT NULL AUTO_INCREMENT,
  `nombre_evento` VARCHAR(60) NULL,
  `fecha_evento` DATE NULL,
  `hora_evento` TIME NULL,
  `clave` VARCHAR(10) NULL,
  `idCategoria` INT NOT NULL,
  `idInvitado` INT NOT NULL,
  PRIMARY KEY (`idEvento`, `categoria_evento_idCategoria`, `idInvitado`),
  INDEX `fk_eventos_categoria_evento_idx` (`categoria_evento_idCategoria` ASC),
  INDEX `fk_eventos_invitados1_idx` (`idInvitado` ASC),
  CONSTRAINT `fk_eventos_categoria_evento`
    FOREIGN KEY (`categoria_evento_idCategoria`)
    REFERENCES `web`.`categoria_evento` (`idCategoria`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_eventos_invitados1`
    FOREIGN KEY (`idInvitado`)
    REFERENCES `web`.`invitados` (`idInvitado`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
