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
CREATE TABLE [stockmarket].[location](
	[location_id] [int] IDENTITY(1,1) NOT NULL,
	[state_id] [int] NULL,
	[country_id] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[location_id] ASC
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
	[location_id] [int] NULL,
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
ALTER TABLE [stockmarket].[location]  WITH CHECK ADD FOREIGN KEY([country_id])
REFERENCES [stockmarket].[country] ([country_id])
GO
ALTER TABLE [stockmarket].[location]  WITH CHECK ADD FOREIGN KEY([state_id])
REFERENCES [stockmarket].[state] ([state_id])
GO
ALTER TABLE [stockmarket].[user]  WITH CHECK ADD FOREIGN KEY([location_id])
REFERENCES [stockmarket].[location] ([location_id])
GO

INSERT INTO stockmarket.country(country_name) values('United States');
INSERT INTO stockmarket.state(state_name) values('Idaho');
INSERT INTO stockmarket.stock(symbol) values('VOO');
INSERT INTO stockmarket.location(country_id, state_id) values ('1', '1')
INSERT INTO stockmarket.[user](first_name, last_name, email, location_id) values('Darwin', 'Porth', 'dporth@gmail.com','1')
INSERT INTO stockmarket.[account](usd_amount, share_amount, stock_id, user_id) values ('500', '1.463151', '1', '1')
INSERT INTO stockmarket.state(state_name) values('New York')
INSERT INTO stockmarket.location(state_id, country_id) values('2', '1')
INSERT [stockmarket].[account_value] ( [account_id], [valid_from], [valid_to], [usd_account_amount]) VALUES (1, CAST(N'2021-01-05T00:50:05.873' AS DateTime), CAST(N'2021-01-05T01:44:13.870' AS DateTime), CAST(496.052084 AS Numeric(38, 6)))
GO
INSERT [stockmarket].[account_value] ( [account_id], [valid_from], [valid_to], [usd_account_amount]) VALUES (1, CAST(N'2021-01-05T01:44:13.880' AS DateTime), CAST(N'2021-01-06T01:11:29.437' AS DateTime), CAST(496.052084 AS Numeric(38, 6)))
GO
INSERT [stockmarket].[account_value] ( [account_id], [valid_from], [valid_to], [usd_account_amount]) VALUES (1, CAST(N'2021-01-06T01:11:29.447' AS DateTime), CAST(N'2021-01-07T03:55:38.137' AS DateTime), CAST(499.314910 AS Numeric(38, 6)))
GO
INSERT [stockmarket].[account_value] ( [account_id], [valid_from], [valid_to], [usd_account_amount]) VALUES (1, CAST(N'2021-01-07T03:55:38.147' AS DateTime), CAST(N'2021-01-08T05:15:08.413' AS DateTime), CAST(502.343633 AS Numeric(38, 6)))
GO
INSERT [stockmarket].[account_value] ( [account_id], [valid_from], [valid_to], [usd_account_amount]) VALUES (1, CAST(N'2021-01-08T05:15:08.417' AS DateTime), CAST(N'2021-01-09T04:12:46.910' AS DateTime), CAST(509.849597 AS Numeric(38, 6)))
GO
INSERT [stockmarket].[account_value] ( [account_id], [valid_from], [valid_to], [usd_account_amount]) VALUES (1, CAST(N'2021-01-09T04:12:46.910' AS DateTime), CAST(N'2021-01-12T01:45:11.307' AS DateTime), CAST(512.717373 AS Numeric(38, 6)))
GO
INSERT [stockmarket].[account_value] ( [account_id], [valid_from], [valid_to], [usd_account_amount]) VALUES (1, CAST(N'2021-01-12T01:45:11.310' AS DateTime), CAST(N'2021-01-13T04:19:54.980' AS DateTime), CAST(509.366758 AS Numeric(38, 6)))
GO
INSERT [stockmarket].[account_value] ( [account_id], [valid_from], [valid_to], [usd_account_amount]) VALUES (1, CAST(N'2021-01-13T04:19:54.990' AS DateTime), NULL, CAST(509.410652 AS Numeric(38, 6)))
GO