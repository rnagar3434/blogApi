-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Jan 25, 2022 at 11:39 AM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `api_project`
--

-- --------------------------------------------------------

--
-- Table structure for table `blog`
--

CREATE TABLE `blog` (
  `id` int(255) NOT NULL,
  `title` varchar(255) NOT NULL,
  `content` text NOT NULL,
  `banner_image` varchar(200) DEFAULT NULL,
  `post_type` varchar(50) NOT NULL,
  `is_published` varchar(50) NOT NULL DEFAULT 'NOT',
  `publish_by` int(255) NOT NULL,
  `archive` tinyint(1) NOT NULL DEFAULT 0,
  `she_time` datetime DEFAULT NULL,
  `status` varchar(20) NOT NULL DEFAULT 'active',
  `publish_date` timestamp NULL DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `blog`
--

INSERT INTO `blog` (`id`, `title`, `content`, `banner_image`, `post_type`, `is_published`, `publish_by`, `archive`, `she_time`, `status`, `publish_date`) VALUES
(1, 'Hello ', 'Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello Hello ', '', 'SHE', 'NOT', 1, 0, NULL, 'inactive', NULL),
(2, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(3, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(4, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(6, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(7, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(8, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(9, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(10, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(11, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(12, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(13, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(14, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(15, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(16, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(17, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(18, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(19, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(20, 'edited', 'dfkrthok gihkjyi tuyituytirjt', NULL, 'SHE', 'YES', 3, 0, '2022-01-24 18:35:00', 'active', '2022-01-24 17:13:29'),
(21, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(23, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(24, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(26, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(27, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(28, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(29, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(30, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(31, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(32, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(33, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(34, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(35, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(36, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(37, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(38, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'inactive', NULL),
(39, 'rohit', 'FG', NULL, 'NOW', 'NOT', 3, 0, '0000-00-00 00:00:00', 'active', '2022-01-24 06:01:16'),
(40, 'rohit', 'FG', NULL, 'NOW', 'YES', 3, 1, '0000-00-00 00:00:00', 'active', '2022-01-24 06:02:40'),
(41, 'rohit FG', 'FG', NULL, 'SHE', 'NOT', 3, 0, '2022-01-24 18:35:00', 'inactive', NULL),
(42, 'hello demo', 'demo demo', NULL, 'NOW', 'YES', 14, 1, '0000-00-00 00:00:00', 'active', '2022-01-25 09:17:02'),
(43, 'hello demo', 'demo demo', NULL, 'SHE', 'YES', 14, 0, '2022-01-25 14:47:00', 'active', '2022-01-25 09:23:28'),
(44, 'She demo updated', 'demo demo', NULL, 'NOW', 'YES', 14, 0, '2022-01-25 15:05:00', 'active', '2022-01-25 09:34:35'),
(46, 'She demo', 'demo demo', NULL, 'SHE', 'YES', 14, 1, '2022-01-25 15:06:00', 'active', '2022-01-25 09:36:34');

-- --------------------------------------------------------

--
-- Table structure for table `user_info`
--

CREATE TABLE `user_info` (
  `id` int(255) NOT NULL,
  `f_name` varchar(60) NOT NULL,
  `s_name` varchar(60) NOT NULL,
  `email` varchar(60) NOT NULL,
  `password` varchar(255) NOT NULL,
  `token` varchar(255) DEFAULT NULL,
  `status` tinyint(4) DEFAULT 1,
  `date_of_creation` timestamp NOT NULL DEFAULT current_timestamp()
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `user_info`
--

INSERT INTO `user_info` (`id`, `f_name`, `s_name`, `email`, `password`, `token`, `status`, `date_of_creation`) VALUES
(1, 'rohit', 'na', 'fd', 'fe', NULL, 1, '2022-01-23 08:15:05'),
(3, 'rohit', 'nagar', 'rnagar3434@gmail.com', '18ac3c1436bb47fbdf3d7b309927404f', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjozLCJleHAiOjE2NDMwNTI5OTh9.Cmdeatw_phV0HaNtdJJBLeeHFbePh9_gOnjtOz4C2pg', 1, '2022-01-23 08:28:17'),
(10, 'rohit', 'nagar', 'rnagar3434@outlook.com', '18ac3c1436bb47fbdf3d7b309927404f', NULL, 1, '2022-01-23 08:42:21'),
(13, 'rohit', 'nagar', 'nupur@gmail.com', '18ac3c1436bb47fbdf3d7b309927404f', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxMywiZXhwIjoxNjQyOTQ0NDkyfQ.S5IIh-wmvB4WOqvVP5UZfT87qkbFVo_FbdQny4IfzvY', 1, '2022-01-23 08:45:25'),
(14, 'Aakash', 'Nagar', 'ak@gmail.com', '18ac3c1436bb47fbdf3d7b309927404f', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNCwiZXhwIjoxNjQzMTEwMDcwfQ.wubDxcrgr7MEvYZHGc7vzhQ-mSLow21W9Y5JxdYAvD8', 1, '2022-01-25 09:02:28'),
(15, 'Rohit', 'Nagar', 'rohit123@gmail.com', '18ac3c1436bb47fbdf3d7b309927404f', 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VyX2lkIjoxNSwiZXhwIjoxNjQzMTExNjE2fQ.HDtXOjfB9OZVWuS-fi_0KyVPJKEYFeP8RlllLEjDQWk', 1, '2022-01-25 09:27:53');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `blog`
--
ALTER TABLE `blog`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user_id` (`publish_by`);

--
-- Indexes for table `user_info`
--
ALTER TABLE `user_info`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `blog`
--
ALTER TABLE `blog`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=47;

--
-- AUTO_INCREMENT for table `user_info`
--
ALTER TABLE `user_info`
  MODIFY `id` int(255) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `blog`
--
ALTER TABLE `blog`
  ADD CONSTRAINT `user_id` FOREIGN KEY (`publish_by`) REFERENCES `user_info` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
