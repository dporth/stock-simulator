USE [PERSONAL]
GO
/****** Object:  Table [stockmarket].[account]    Script Date: 1/2/2021 10:14:57 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[account](
	[account_id] [int] IDENTITY(1,1) NOT NULL,
	[usd_amount] [numeric](38, 6) NULL,
	[share_amount] [numeric](38, 6) NULL,
	[user_id] [int] NULL,
	[stock_id] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[account_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[account_value]    Script Date: 1/2/2021 10:14:57 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[account_value](
	[account_value_id] [int] IDENTITY(1,1) NOT NULL,
	[account_id] [int] NULL,
	[valid_from] [datetime] NULL,
	[valid_to] [datetime] NULL,
	[usd_account_amount] [numeric](38, 6) NULL,
PRIMARY KEY CLUSTERED 
(
	[account_value_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[address]    Script Date: 1/2/2021 10:14:57 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[address](
	[address_id] [int] IDENTITY(1,1) NOT NULL,
	[street] [nvarchar](1000) NULL,
	[postal_code] [nvarchar](50) NULL,
	[city_id] [int] NULL,
	[state_id] [int] NULL,
	[country_id] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[address_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[city]    Script Date: 1/2/2021 10:14:57 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[city](
	[city_id] [int] IDENTITY(1,1) NOT NULL,
	[city_name] [nvarchar](256) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[city_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[country]    Script Date: 1/2/2021 10:14:57 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[country](
	[country_id] [int] IDENTITY(1,1) NOT NULL,
	[country_name] [nvarchar](256) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[country_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[state]    Script Date: 1/2/2021 10:14:57 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[state](
	[state_id] [int] IDENTITY(1,1) NOT NULL,
	[state_name] [nvarchar](256) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[state_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[stock]    Script Date: 1/2/2021 10:14:57 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[stock](
	[stock_id] [int] IDENTITY(1,1) NOT NULL,
	[symbol] [nvarchar](50) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[stock_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[user]    Script Date: 1/2/2021 10:14:57 AM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[user](
	[user_id] [int] IDENTITY(1,1) NOT NULL,
	[first_name] [nvarchar](1000) NULL,
	[last_name] [nvarchar](50) NULL,
	email [nvarchar](320) NULL,
	[address_id] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [stockmarket].[account_value] ADD  DEFAULT (getdate()) FOR [valid_from]
GO
ALTER TABLE [stockmarket].[account_value]  WITH CHECK ADD FOREIGN KEY([account_id])
REFERENCES [stockmarket].[account] ([account_id])
GO
ALTER TABLE [stockmarket].[account]  WITH CHECK ADD FOREIGN KEY([stock_id])
REFERENCES [stockmarket].[stock] ([stock_id])
GO
ALTER TABLE [stockmarket].[account]  WITH CHECK ADD FOREIGN KEY([user_id])
REFERENCES [stockmarket].[user] ([user_id])
GO
ALTER TABLE [stockmarket].[address]  WITH CHECK ADD FOREIGN KEY([city_id])
REFERENCES [stockmarket].[city] ([city_id])
GO
ALTER TABLE [stockmarket].[address]  WITH CHECK ADD FOREIGN KEY([country_id])
REFERENCES [stockmarket].[country] ([country_id])
GO
ALTER TABLE [stockmarket].[address]  WITH CHECK ADD FOREIGN KEY([state_id])
REFERENCES [stockmarket].[state] ([state_id])
GO
ALTER TABLE [stockmarket].[user]  WITH CHECK ADD FOREIGN KEY([address_id])
REFERENCES [stockmarket].[address] ([address_id])
GO

INSERT INTO stockmarket.city(city_name) values('Boise');
INSERT INTO stockmarket.country(country_name) values('United States');
INSERT INTO stockmarket.state(state_name) values('Idaho');
INSERT INTO stockmarket.stock(symbol) values('VOO');
INSERT INTO stockmarket.address(street,postal_code, country_id, state_id, city_id) values ('5437 South Begonia Place', '83716', '1', '1', '1')
INSERT INTO stockmarket.[user](first_name, last_name, email, address_id) values('Darwin', 'Porth', 'dporth@gmail.com','1')
INSERT INTO stockmarket.[account](usd_amount, share_amount, stock_id, user_id) values ('500', '1.463151', '1', '1')
INSERT INTO stockmarket.state(state_name) values('New York')
INSERT INTO stockmarket.city(city_name) values('New York')
INSERT INTO stockmarket.address(street, postal_code, city_id, state_id, country_id) values('1 Centre St, New York', '10007', '2', '2', '1')