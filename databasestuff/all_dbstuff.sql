CREATE TABLE `itemlistings_category` (
  `categoryID` int unsigned NOT NULL AUTO_INCREMENT,
  `categoryName` varchar(70) NOT NULL,
  PRIMARY KEY (`categoryID`),
  UNIQUE KEY `categoryID_UNIQUE` (`categoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `itemlistings_main` (
  `itemID` int unsigned NOT NULL AUTO_INCREMENT,
  `itemName` varchar(75) NOT NULL,
  `Distributer` varchar(75) NOT NULL,
  `imagepath` varchar(200) DEFAULT NULL,
  `categoryID` int unsigned NOT NULL DEFAULT '4',
  `price` float NOT NULL,
  `manufacture` varchar(75) DEFAULT NULL,
  `lastModifed` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`itemID`),
  UNIQUE KEY `itemID_UNIQUE` (`itemID`),
  KEY `categoryID_idx` (`categoryID`),
  KEY `categorymain_idx` (`categoryID`),
  CONSTRAINT `categorymain` FOREIGN KEY (`categoryID`) REFERENCES `itemlistings_category` (`categoryID`)
) ENGINE=InnoDB AUTO_INCREMENT=169 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `itemlistings_cart` (
  `cartID` int unsigned NOT NULL AUTO_INCREMENT,
  `userName` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `pickupdelv` tinyint NOT NULL,
  `address` varchar(100) DEFAULT NULL,
  `LastModified` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`cartID`),
  UNIQUE KEY `cartID_UNIQUE` (`cartID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
CREATE TABLE `itemlistings_cartitem` (
  `cartitemID` int unsigned NOT NULL AUTO_INCREMENT,
  `cartID` int unsigned NOT NULL,
  `itemID` int unsigned NOT NULL,
  `quantity` int unsigned NOT NULL,
  `lbwanted` float unsigned DEFAULT NULL,
  `last_modifed` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`cartitemID`),
  UNIQUE KEY `cartitemID_UNIQUE` (`cartitemID`),
  KEY `cartitemmain_idx` (`itemID`),
  KEY `cartitemcart_idx` (`cartID`),
  CONSTRAINT `cartitemcart` FOREIGN KEY (`cartID`) REFERENCES `itemlistings_cart` (`cartID`),
  CONSTRAINT `cartitemmain` FOREIGN KEY (`itemID`) REFERENCES `itemlistings_main` (`itemID`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;