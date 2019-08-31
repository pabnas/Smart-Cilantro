-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Servidor: localhost:3306
-- Tiempo de generación: 26-06-2019 a las 13:06:39
-- Versión del servidor: 5.7.25-0ubuntu0.18.04.2
-- Versión de PHP: 7.2.15-0ubuntu0.18.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `smart_cilantro`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Mediciones`
--

CREATE TABLE IF NOT EXISTS `Mediciones` (
  `id_Planta` int(11) NOT NULL,
  `fecha` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  `humedad` float DEFAULT NULL,
  `temperatura` float DEFAULT NULL,
  `polucion` float DEFAULT NULL,
  `nivelbajo` float DEFAULT NULL,
  `nivelalto` float DEFAULT NULL,
  `luz` float DEFAULT NULL,
  KEY `ID` (`id_Planta`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Mediciones`
--

INSERT INTO `Mediciones` (`id_Planta`, `fecha`, `humedad`, `temperatura`, `polucion`, `nivelbajo`, `nivelalto`, `luz`) VALUES
(1, '2019-06-11 14:15:53', 698, 20.125, 28, 1, 1, 443),
(1, '2019-06-11 14:15:55', 698, 20.125, 28, 1, 1, 443),
(1, '2019-06-11 14:15:57', 698, 20.125, 28, 1, 1, 447),
(1, '2019-06-11 14:15:59', 698, 20.125, 28, 1, 1, 446),
(1, '2019-06-11 14:16:01', 698, 20.125, 28, 1, 1, 448),
(1, '2019-06-11 14:16:03', 698, 20.125, 28, 1, 1, 451),
(1, '2019-06-11 14:16:06', 704, 20.125, 28, 1, 1, 456),
(1, '2019-06-11 14:16:08', 698, 20.125, 28, 1, 1, 457),
(1, '2019-06-11 14:16:10', 698, 20.125, 28, 1, 1, 460),
(1, '2019-06-11 14:16:11', 698, 20.125, 28, 1, 1, 458),
(1, '2019-06-11 14:16:13', 698, 20.562, 28, 1, 1, 455),
(1, '2019-06-11 14:16:15', 698, 21.062, 28, 1, 1, 455),
(1, '2019-06-11 14:16:17', 698, 21.5, 28, 1, 1, 455),
(1, '2019-06-11 14:16:19', 699, 21.875, 28, 1, 1, 267),
(1, '2019-06-11 14:16:21', 698, 22.187, 27, 1, 1, 34),
(1, '2019-06-11 14:16:23', 698, 22.437, 28, 1, 1, 31),
(1, '2019-06-11 14:16:26', 699, 22.75, 28, 1, 1, 9),
(1, '2019-06-11 14:16:28', 700, 23, 28, 1, 1, 11),
(1, '2019-06-11 14:16:30', 700, 23.187, 28, 1, 1, 25),
(1, '2019-06-11 14:16:32', 697, 23.437, 30, 1, 1, 13),
(1, '2019-06-11 14:16:34', 698, 23.75, 30, 1, 1, 12),
(1, '2019-06-11 14:16:36', 699, 24, 30, 1, 1, 473),
(1, '2019-06-11 14:16:38', 700, 24.25, 30, 1, 1, 470),
(1, '2019-06-11 14:16:40', 698, 24.5, 30, 1, 1, 473),
(1, '2019-06-11 14:16:42', 698, 24.687, 30, 1, 1, 473),
(1, '2019-06-11 14:36:23', 711, 19.875, 28, 1, 1, 470),
(1, '2019-06-11 14:36:25', 708, 19.875, 28, 1, 1, 475),
(1, '2019-06-11 14:38:30', 709, 24.375, 30, 1, 1, 454),
(1, '2019-06-11 14:38:42', 707, 24, 30, 1, 1, 485),
(1, '2019-06-11 14:38:44', 715, 23.937, 29, 1, 1, 478),
(1, '2019-06-11 14:38:46', 716, 23.875, 30, 1, 1, 479),
(1, '2019-06-11 14:38:48', 709, 23.875, 29, 1, 1, 482),
(1, '2019-06-11 14:38:50', 705, 23.812, 30, 1, 1, 479),
(1, '2019-06-11 14:38:52', 710, 23.75, 31, 1, 1, 474),
(1, '2019-06-11 14:38:54', 706, 23.687, 29, 1, 1, 473),
(1, '2019-06-11 14:38:56', 706, 23.625, 30, 1, 1, 471),
(1, '2019-06-11 14:38:58', 711, 23.625, 31, 1, 1, 469),
(1, '2019-06-11 14:39:00', 715, 23.562, 31, 1, 1, 470),
(1, '2019-06-11 14:39:02', 710, 23.5, 30, 1, 1, 476),
(1, '2019-06-11 14:39:04', 705, 23.437, 30, 1, 1, 474),
(1, '2019-06-11 14:39:06', 711, 23.437, 30, 1, 1, 475),
(1, '2019-06-11 14:39:08', 706, 23.375, 30, 1, 1, 483),
(1, '2019-06-11 14:39:10', 707, 23.312, 30, 1, 1, 476),
(1, '2019-06-11 14:39:12', 709, 23.25, 30, 1, 1, 343),
(1, '2019-06-11 14:39:14', 714, 23.25, 31, 1, 1, 362),
(1, '2019-06-11 14:39:16', 708, 23.187, 30, 1, 1, 477),
(1, '2019-06-11 14:39:18', 715, 23.125, 31, 1, 1, 457),
(1, '2019-06-11 14:39:20', 708, 23.125, 31, 1, 1, 453),
(1, '2019-06-11 14:39:22', 713, 23.062, 31, 1, 1, 453),
(1, '2019-06-11 14:39:24', 708, 23, 33, 1, 1, 467),
(1, '2019-06-11 14:39:26', 707, 23, 32, 1, 1, 454),
(1, '2019-06-11 14:39:29', 710, 22.937, 31, 1, 1, 450),
(1, '2019-06-11 14:39:31', 707, 22.875, 31, 1, 1, 448),
(1, '2019-06-11 14:39:33', 706, 22.875, 31, 1, 1, 449),
(1, '2019-06-11 14:39:35', 714, 22.812, 30, 1, 1, 449),
(1, '2019-06-11 14:39:37', 715, 22.75, 30, 1, 1, 449),
(1, '2019-06-11 14:39:39', 706, 22.75, 29, 1, 1, 450),
(1, '2019-06-11 14:39:41', 706, 22.687, 31, 1, 1, 450),
(1, '2019-06-11 14:39:43', 706, 22.687, 30, 1, 1, 450),
(1, '2019-06-11 14:39:45', 707, 22.625, 31, 1, 1, 450),
(1, '2019-06-11 14:41:01', 712, 21.562, 29, 1, 1, 486),
(1, '2019-06-11 14:41:03', 707, 21.562, 29, 1, 1, 485),
(1, '2019-06-11 14:42:33', 706, 20.812, 28, 1, 1, 468),
(1, '2019-06-11 14:42:35', 713, 20.812, 31, 1, 1, 467),
(1, '2019-06-11 14:42:37', 709, 20.812, 29, 1, 1, 278),
(1, '2019-06-11 14:42:39', 704, 20.75, 31, 1, 1, 380),
(1, '2019-06-11 14:42:41', 709, 20.75, 30, 1, 1, 203),
(1, '2019-06-11 14:42:43', 709, 20.75, 30, 1, 1, 469),
(1, '2019-06-11 14:42:45', 708, 20.75, 30, 1, 1, 469),
(1, '2019-06-11 14:42:47', 709, 20.75, 29, 1, 1, 465),
(1, '2019-06-11 14:42:49', 706, 20.75, 30, 1, 1, 460),
(1, '2019-06-11 14:42:51', 706, 20.687, 30, 1, 1, 460),
(1, '2019-06-11 14:42:53', 704, 20.687, 29, 1, 1, 458),
(1, '2019-06-11 14:42:55', 705, 20.687, 29, 1, 1, 457),
(1, '2019-06-11 14:42:57', 709, 20.687, 30, 1, 1, 458),
(1, '2019-06-11 14:42:59', 713, 20.687, 31, 1, 1, 458),
(1, '2019-06-11 14:43:01', 711, 20.625, 31, 1, 1, 458),
(1, '2019-06-11 14:43:03', 708, 20.625, 30, 1, 1, 460),
(1, '2019-06-11 14:43:05', 712, 20.625, 30, 1, 1, 459),
(1, '2019-06-11 14:43:07', 705, 20.625, 28, 1, 1, 459),
(1, '2019-06-11 14:43:09', 704, 20.625, 30, 1, 1, 460),
(1, '2019-06-11 14:43:11', 709, 20.625, 28, 1, 1, 459),
(1, '2019-06-11 14:43:13', 709, 20.625, 31, 1, 1, 463),
(1, '2019-06-11 14:43:15', 709, 20.562, 30, 1, 1, 460),
(1, '2019-06-11 14:43:17', 715, 20.562, 30, 1, 1, 460),
(1, '2019-06-11 14:43:19', 705, 20.562, 31, 1, 1, 459),
(1, '2019-06-11 14:43:21', 711, 20.562, 31, 1, 1, 460),
(1, '2019-06-11 14:43:23', 709, 20.562, 30, 1, 1, 460),
(1, '2019-06-11 14:43:25', 705, 20.562, 30, 1, 1, 471),
(1, '2019-06-11 14:43:27', 706, 20.5, 31, 1, 1, 486),
(1, '2019-06-11 14:43:29', 705, 20.5, 31, 1, 1, 486),
(1, '2019-06-11 14:43:31', 708, 20.5, 31, 1, 1, 487),
(1, '2019-06-11 14:43:33', 716, 20.5, 31, 1, 1, 483),
(1, '2019-06-11 14:43:35', 715, 20.5, 30, 1, 1, 473),
(1, '2019-06-11 14:43:37', 715, 20.5, 30, 1, 1, 467),
(1, '2019-06-11 14:43:39', 709, 20.5, 32, 1, 1, 467),
(1, '2019-06-11 14:43:41', 709, 20.5, 30, 1, 1, 469),
(1, '2019-06-11 14:43:43', 708, 20.437, 31, 1, 1, 462),
(1, '2019-06-11 14:43:45', 708, 20.437, 31, 1, 1, 460),
(1, '2019-06-11 14:43:47', 713, 20.437, 31, 1, 1, 459),
(1, '2019-06-11 14:43:49', 708, 20.437, 31, 1, 1, 458),
(1, '2019-06-11 14:43:51', 706, 20.437, 31, 1, 1, 457),
(1, '2019-06-11 14:43:53', 706, 20.437, 31, 1, 1, 456),
(1, '2019-06-11 14:43:56', 706, 20.437, 31, 1, 1, 455),
(1, '2019-06-11 14:43:58', 710, 20.437, 31, 1, 1, 457),
(1, '2019-06-11 14:44:00', 710, 20.375, 31, 1, 1, 457),
(1, '2019-06-11 14:44:02', 713, 20.375, 31, 1, 1, 459),
(1, '2019-06-11 14:44:04', 709, 20.375, 31, 1, 1, 463),
(1, '2019-06-11 14:44:07', 707, 20.375, 31, 1, 1, 466),
(1, '2019-06-11 14:44:09', 707, 20.375, 31, 1, 1, 465),
(1, '2019-06-11 14:44:11', 705, 20.375, 31, 1, 1, 456),
(1, '2019-06-11 14:44:13', 708, 20.375, 31, 1, 1, 456),
(1, '2019-06-11 14:44:15', 710, 20.375, 32, 1, 1, 455),
(1, '2019-06-11 14:44:17', 713, 20.312, 30, 1, 1, 454),
(1, '2019-06-11 14:44:20', 708, 20.312, 30, 1, 1, 453),
(1, '2019-06-11 14:44:22', 713, 20.312, 31, 1, 1, 453),
(1, '2019-06-11 14:44:24', 712, 20.312, 31, 1, 1, 454),
(1, '2019-06-11 14:44:26', 705, 20.312, 32, 1, 1, 453),
(1, '2019-06-11 14:44:28', 708, 20.312, 31, 1, 1, 453),
(1, '2019-06-11 14:44:30', 705, 20.312, 31, 1, 1, 453),
(1, '2019-06-11 14:44:33', 710, 20.312, 31, 1, 1, 453),
(1, '2019-06-11 14:44:35', 714, 20.312, 32, 1, 1, 452),
(1, '2019-06-11 14:44:37', 716, 20.312, 31, 1, 1, 453),
(1, '2019-06-11 14:44:39', 705, 20.25, 31, 1, 1, 452),
(1, '2019-06-11 14:44:41', 705, 20.25, 31, 1, 1, 452),
(1, '2019-06-11 14:44:43', 704, 20.25, 31, 1, 1, 453),
(1, '2019-06-11 14:44:45', 705, 20.25, 33, 1, 1, 451),
(1, '2019-06-11 14:44:47', 705, 20.25, 30, 1, 1, 452),
(1, '2019-06-11 14:44:49', 704, 20.25, 32, 1, 1, 452),
(1, '2019-06-11 14:44:51', 714, 20.25, 32, 1, 1, 451),
(1, '2019-06-11 14:44:53', 713, 20.25, 31, 1, 1, 451),
(1, '2019-06-11 14:44:55', 705, 20.25, 31, 1, 1, 451);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Planta`
--

CREATE TABLE IF NOT EXISTS `Planta` (
  `ID` int(11) NOT NULL,
  `tipo` text NOT NULL,
  `fecha_plantado` datetime NOT NULL,
  `proveedor` text NOT NULL,
  `id_plantador` int(11) NOT NULL,
  `Id_tecnica` int(11) NOT NULL,
  `Ruta_camara` text,
  PRIMARY KEY (`ID`),
  KEY `id_plantador` (`id_plantador`),
  KEY `id_plantador_2` (`id_plantador`),
  KEY `Id_tecnica` (`Id_tecnica`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Planta`
--

INSERT INTO `Planta` (`ID`, `tipo`, `fecha_plantado`, `proveedor`, `id_plantador`, `Id_tecnica`, `Ruta_camara`) VALUES
(1, 'Cilantro', '2019-04-12 10:00:00', 'Carolina', 2, 3, '192.168.0.12:8080');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Tecnicas`
--

CREATE TABLE IF NOT EXISTS `Tecnicas` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Nombre de metodo` varchar(50) NOT NULL,
  `Recipiente` varchar(50) DEFAULT NULL,
  `Descipcion` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Tecnicas`
--

INSERT INTO `Tecnicas` (`ID`, `Nombre de metodo`, `Recipiente`, `Descipcion`) VALUES
(1, 'Tubulares', 'Vertical', NULL),
(2, 'Cojin', 'Horizontal', NULL),
(3, 'Botellas o Materas', 'Individuales pequeños', NULL),
(4, 'Canecas Plásticas', 'Individuales', NULL),
(5, 'Canecas Plásticas', 'Individuales', NULL),
(6, 'Camas', 'Horizontal', NULL);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Usuario`
--

CREATE TABLE IF NOT EXISTS `Usuario` (
  `ID` int(11) NOT NULL AUTO_INCREMENT,
  `Username` text NOT NULL,
  `Nombre` text NOT NULL,
  `Apellidos` text,
  `Password` text NOT NULL,
  `Privilegios` int(11) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID` (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Usuario`
--

INSERT INTO `Usuario` (`ID`, `Username`, `Nombre`, `Apellidos`, `Password`, `Privilegios`) VALUES
(1, 'santiagobarragan@usantotomas.edu.co', 'Santiago', 'Barragan Paez', '071930', 1),
(2, 'carolinagomezr@usantotomas.edu.co', 'Carolina', 'Gomez', '1234', 1),
(5, 'Alison_Ruiz', 'Alison', 'Ruiz', '1234', 2);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `Usuario_Planta`
--

CREATE TABLE IF NOT EXISTS `Usuario_Planta` (
  `id_Planta` int(11) DEFAULT NULL,
  `id_Usuario` int(11) DEFAULT NULL,
  KEY `FK_planta` (`id_Planta`),
  KEY `FK_user` (`id_Usuario`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Volcado de datos para la tabla `Usuario_Planta`
--

INSERT INTO `Usuario_Planta` (`id_Planta`, `id_Usuario`) VALUES
(1, 1),
(1, 2);

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `Mediciones`
--
ALTER TABLE `Mediciones`
  ADD CONSTRAINT `Mediciones_ibfk_1` FOREIGN KEY (`id_Planta`) REFERENCES `Planta` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `Planta`
--
ALTER TABLE `Planta`
  ADD CONSTRAINT `id usuario` FOREIGN KEY (`id_plantador`) REFERENCES `Usuario` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `id_tecnica` FOREIGN KEY (`Id_tecnica`) REFERENCES `Tecnicas` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

--
-- Filtros para la tabla `Usuario_Planta`
--
ALTER TABLE `Usuario_Planta`
  ADD CONSTRAINT `Planta` FOREIGN KEY (`id_Planta`) REFERENCES `Planta` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `User` FOREIGN KEY (`id_Usuario`) REFERENCES `Usuario` (`ID`) ON DELETE CASCADE ON UPDATE CASCADE;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
