USE [STS]
GO
ALTER TABLE [stockmarket].[stock_price_queue] DROP CONSTRAINT [FK__stock_pri__stock__0F624AF8]
GO
ALTER TABLE [stockmarket].[stock_price_history] DROP CONSTRAINT [FK__stock_pri__stock__0E6E26BF]
GO
ALTER TABLE [stockmarket].[account_value_queue_updated] DROP CONSTRAINT [FK__account_v__accou__0D7A0286]
GO
ALTER TABLE [stockmarket].[account_value] DROP CONSTRAINT [FK__account_v__accou__0C85DE4D]
GO
ALTER TABLE [stockmarket].[account] DROP CONSTRAINT [FK__account__user_id__0B91BA14]
GO
ALTER TABLE [stockmarket].[account] DROP CONSTRAINT [FK__account__user_id__0A9D95DB]
GO
ALTER TABLE [stockmarket].[account] DROP CONSTRAINT [FK__account__stock_i__09A971A2]
GO
ALTER TABLE [stockmarket].[account] DROP CONSTRAINT [FK__account__stock_i__08B54D69]
GO
ALTER TABLE [stockmarket].[stock_price_queue] DROP CONSTRAINT [DF__stock_pri__etl_d__07C12930]
GO
ALTER TABLE [stockmarket].[stock_price_history] DROP CONSTRAINT [DF__stock_pri__valid__06CD04F7]
GO
ALTER TABLE [stockmarket].[account_value_queue_updated] DROP CONSTRAINT [DF__account_v__etl_d__05D8E0BE]
GO
ALTER TABLE [stockmarket].[account_value] DROP CONSTRAINT [DF__account_v__valid__04E4BC85]
GO
ALTER TABLE [stockmarket].[account] DROP CONSTRAINT [DF__account__create___03F0984C]
GO
/****** Object:  Table [stockmarket].[user]    Script Date: 4/10/2021 12:15:17 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[stockmarket].[user]') AND type in (N'U'))
DROP TABLE [stockmarket].[user]
GO
/****** Object:  Table [stockmarket].[stock_price_queue]    Script Date: 4/10/2021 12:15:17 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[stockmarket].[stock_price_queue]') AND type in (N'U'))
DROP TABLE [stockmarket].[stock_price_queue]
GO
/****** Object:  Table [stockmarket].[stock_price_history]    Script Date: 4/10/2021 12:15:17 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[stockmarket].[stock_price_history]') AND type in (N'U'))
DROP TABLE [stockmarket].[stock_price_history]
GO
/****** Object:  Table [stockmarket].[stock]    Script Date: 4/10/2021 12:15:17 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[stockmarket].[stock]') AND type in (N'U'))
DROP TABLE [stockmarket].[stock]
GO
/****** Object:  Table [stockmarket].[account_value_queue_updated]    Script Date: 4/10/2021 12:15:17 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[stockmarket].[account_value_queue_updated]') AND type in (N'U'))
DROP TABLE [stockmarket].[account_value_queue_updated]
GO
/****** Object:  Table [stockmarket].[account_value]    Script Date: 4/10/2021 12:15:17 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[stockmarket].[account_value]') AND type in (N'U'))
DROP TABLE [stockmarket].[account_value]
GO
/****** Object:  Table [stockmarket].[account]    Script Date: 4/10/2021 12:15:17 PM ******/
IF  EXISTS (SELECT * FROM sys.objects WHERE object_id = OBJECT_ID(N'[stockmarket].[account]') AND type in (N'U'))
DROP TABLE [stockmarket].[account]
GO
/****** Object:  Table [stockmarket].[account]    Script Date: 4/10/2021 12:15:17 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[account](
	[account_id] [int] IDENTITY(1,1) NOT NULL,
	[share_price] [numeric](38, 6) NULL,
	[share_amount] [numeric](38, 6) NULL,
	[user_id] [nvarchar](256) NULL,
	[stock_id] [int] NULL,
	[create_date] [datetime] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[account_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[account_value]    Script Date: 4/10/2021 12:15:18 PM ******/
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
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[account_value_queue_updated]    Script Date: 4/10/2021 12:15:18 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[account_value_queue_updated](
	[queue_updated_id] [int] IDENTITY(1,1) NOT NULL,
	[account_value_id] [int] NOT NULL,
	[etl_date] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[stock]    Script Date: 4/10/2021 12:15:18 PM ******/
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
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[stock_price_history]    Script Date: 4/10/2021 12:15:18 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[stock_price_history](
	[stock_price_history_id] [int] IDENTITY(1,1) NOT NULL,
	[stock_id] [int] NOT NULL,
	[historical_usd_price] [numeric](38, 6) NOT NULL,
	[valid_from] [datetime] NULL,
	[valid_to] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[stock_price_queue]    Script Date: 4/10/2021 12:15:18 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[stock_price_queue](
	[queue_id] [int] IDENTITY(1,1) NOT NULL,
	[stock_id] [int] NOT NULL,
	[etl_date] [datetime] NULL
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[user]    Script Date: 4/10/2021 12:15:18 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[user](
	[user_id] [nvarchar](256) NOT NULL,
	[identifier] [nvarchar](320) NULL,
PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [stockmarket].[account] ADD  DEFAULT (getdate()) FOR [create_date]
GO
ALTER TABLE [stockmarket].[account_value] ADD  DEFAULT (getdate()) FOR [valid_from]
GO
ALTER TABLE [stockmarket].[account_value_queue_updated] ADD  DEFAULT (getdate()) FOR [etl_date]
GO
ALTER TABLE [stockmarket].[stock_price_history] ADD  DEFAULT (getdate()) FOR [valid_from]
GO
ALTER TABLE [stockmarket].[stock_price_queue] ADD  DEFAULT (getdate()) FOR [etl_date]
GO
ALTER TABLE [stockmarket].[account]  WITH CHECK ADD FOREIGN KEY([stock_id])
REFERENCES [stockmarket].[stock] ([stock_id])
GO
ALTER TABLE [stockmarket].[account]  WITH CHECK ADD FOREIGN KEY([stock_id])
REFERENCES [stockmarket].[stock] ([stock_id])
GO
ALTER TABLE [stockmarket].[account]  WITH CHECK ADD FOREIGN KEY([user_id])
REFERENCES [stockmarket].[user] ([user_id])
GO
ALTER TABLE [stockmarket].[account]  WITH CHECK ADD FOREIGN KEY([user_id])
REFERENCES [stockmarket].[user] ([user_id])
GO
ALTER TABLE [stockmarket].[account_value]  WITH CHECK ADD FOREIGN KEY([account_id])
REFERENCES [stockmarket].[account] ([account_id])
GO
ALTER TABLE [stockmarket].[account_value_queue_updated]  WITH CHECK ADD FOREIGN KEY([account_value_id])
REFERENCES [stockmarket].[account_value] ([account_value_id])
GO
ALTER TABLE [stockmarket].[stock_price_history]  WITH CHECK ADD FOREIGN KEY([stock_id])
REFERENCES [stockmarket].[stock] ([stock_id])
GO
ALTER TABLE [stockmarket].[stock_price_queue]  WITH CHECK ADD FOREIGN KEY([stock_id])
REFERENCES [stockmarket].[stock] ([stock_id])
GO
