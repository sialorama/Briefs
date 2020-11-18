-- phpMyAdmin SQL Dump
-- version 4.9.5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Oct 29, 2020 at 06:24 PM
-- Server version: 5.7.24
-- PHP Version: 7.4.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `binomotron`
--

-- --------------------------------------------------------

--
-- Table structure for table `apprenants`
--

CREATE TABLE `apprenants` (
  `id_apprenants` int(11) NOT NULL,
  `nom` varchar(50) NOT NULL,
  `prenom` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `apprenants`
--

INSERT INTO `apprenants` (`id_apprenants`, `nom`, `prenom`) VALUES
(1, 'Bonneau', 'Amaury'),
(2, 'Pertron', 'Aude'),
(3, 'Le Berre', 'Baptiste LB'),
(4, 'Le Goff', 'Baptiste LG'),
(5, 'Guillen', 'Celine'),
(6, 'Karfaoui', 'Christelle'),
(7, 'Mbarga Mvogo', 'Christian'),
(8, 'Cloatre', 'Erwan'),
(9, 'Moulard', 'Eva'),
(10, 'Verpoest', 'Guillaume'),
(11, 'Ibanni', 'Jamal'),
(12, 'Le Joncour', 'Jeremy'),
(13, 'Furiga', 'Julien'),
(14, 'Maintier', 'Ludivine'),
(15, 'Bokalli', 'Luigi'),
(16, 'Sabia', 'Paul'),
(17, 'Le Moal', 'Patricia'),
(18, 'Hergoualc\'h', 'Pereg'),
(19, 'Rioual', 'Ronan'),
(20, 'Chaigneau', 'Thomas');

-- --------------------------------------------------------

--
-- Table structure for table `apprenant_groupe`
--

CREATE TABLE `apprenant_groupe` (
  `id_apprenants` int(11) NOT NULL,
  `id_projet` int(11) NOT NULL,
  `id_groupe` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `apprenant_groupe`
--

INSERT INTO `apprenant_groupe` (`id_apprenants`, `id_projet`, `id_groupe`) VALUES
(3, 1, 1),
(14, 1, 1),
(2, 1, 2),
(6, 1, 2),
(4, 1, 3),
(9, 1, 3),
(19, 1, 4),
(11, 1, 4),
(20, 1, 5),
(18, 1, 5),
(16, 1, 6),
(10, 1, 6),
(7, 1, 7),
(15, 1, 7),
(12, 1, 8),
(1, 1, 8),
(8, 1, 9),
(5, 1, 9),
(13, 1, 10),
(17, 1, 10);

-- --------------------------------------------------------

--
-- Table structure for table `groupe`
--

CREATE TABLE `groupe` (
  `id_groupe` int(11) NOT NULL,
  `libelle_groupe` varchar(50) NOT NULL,
  `groupe_constitue` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `groupe`
--

INSERT INTO `groupe` (`id_groupe`, `libelle_groupe`, `groupe_constitue`) VALUES
(1, 'Groupe1', ''),
(2, 'Groupe2', ''),
(3, 'Groupe3', ''),
(4, 'Groupe4', ''),
(5, 'Groupe5', ''),
(6, 'Groupe6', ''),
(7, 'Groupe7', ''),
(8, 'Groupe8', ''),
(9, 'Groupe9', ''),
(10, 'Groupe10', '');

-- --------------------------------------------------------

--
-- Table structure for table `projet`
--

CREATE TABLE `projet` (
  `id_projet` int(11) NOT NULL,
  `libelle_projet` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Dumping data for table `projet`
--

INSERT INTO `projet` (`id_projet`, `libelle_projet`) VALUES
(1, 'Veille IA'),
(2, 'Kata');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `apprenants`
--
ALTER TABLE `apprenants`
  ADD PRIMARY KEY (`id_apprenants`);

--
-- Indexes for table `apprenant_groupe`
--
ALTER TABLE `apprenant_groupe`
  ADD KEY `id_apprenant` (`id_apprenants`),
  ADD KEY `apprenant_groupe_ibfk_2` (`id_projet`),
  ADD KEY `apprenant_groupe_ibfk_3` (`id_groupe`);

--
-- Indexes for table `groupe`
--
ALTER TABLE `groupe`
  ADD PRIMARY KEY (`id_groupe`);

--
-- Indexes for table `projet`
--
ALTER TABLE `projet`
  ADD PRIMARY KEY (`id_projet`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `apprenants`
--
ALTER TABLE `apprenants`
  MODIFY `id_apprenants` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;

--
-- AUTO_INCREMENT for table `groupe`
--
ALTER TABLE `groupe`
  MODIFY `id_groupe` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `projet`
--
ALTER TABLE `projet`
  MODIFY `id_projet` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `apprenant_groupe`
--
ALTER TABLE `apprenant_groupe`
  ADD CONSTRAINT `apprenant_groupe_ibfk_1` FOREIGN KEY (`id_apprenants`) REFERENCES `apprenants` (`id_apprenants`),
  ADD CONSTRAINT `apprenant_groupe_ibfk_2` FOREIGN KEY (`id_projet`) REFERENCES `projet` (`id_projet`),
  ADD CONSTRAINT `apprenant_groupe_ibfk_3` FOREIGN KEY (`id_groupe`) REFERENCES `groupe` (`id_groupe`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
