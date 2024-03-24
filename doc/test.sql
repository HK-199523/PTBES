CREATE TABLE User (
  CreationDate DATETIME,
  UpdateDate DATETIME,
  UserID INT,
  UserName VARCHAR(255)
);

CREATE TABLE News (
  CreationDate DATETIME,
  UpdateDate DATETIME,
  NewsID INT,
  Title VARCHAR(255),
  Content TEXT,
  UserID INT
);

CREATE TABLE ExchangeRate (
  CreationDate DATETIME,
  UpdateDate DATETIME,
  CountryCode VARCHAR(255),
  UnitCode VARCHAR(255),
  ExchangeRate DECIMAL(10, 2)
);

CREATE TABLE Country (
  CreationDate DATETIME,
  UpdateDate DATETIME,
  CountryCode VARCHAR(255),
  CountryName VARCHAR(255),
  RegionCode VARCHAR(255),
  AverageIncome DECIMAL(10, 2)
);

CREATE TABLE Region (
  CreationDate DATETIME,
  UpdateDate DATETIME,
  RegionCode VARCHAR(255),
  RegionName VARCHAR(255)
);

CREATE TABLE Unit (
  CreationDate DATETIME,
  UpdateDate DATETIME,
  UnitCode VARCHAR(255),
  UnitName VARCHAR(255)
);

CREATE TABLE TouristSpot (
  CreationDate DATETIME,
  UpdateDate DATETIME,
  CountryCode VARCHAR(255),
  TouristSpotName VARCHAR(255),
  TouristSpotCode VARCHAR(255),
  TouristSpotDescription TEXT,
  ImageURL VARCHAR(255),
  URL1 VARCHAR(255),
  URL2 VARCHAR(255),
  URL3 VARCHAR(255),
  URL4 VARCHAR(255),
  URL5 VARCHAR(255),
  DisplayFlag BOOLEAN,
  UserID INT
);
