/****** Object:  Table [stockmarket].[account]    Script Date: 2/13/2021 5:38:48 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[account](
	[account_id] [int] IDENTITY(1,1) NOT NULL,
	[usd_amount] [numeric](38, 6) NULL,
	[share_amount] [numeric](38, 6) NULL,
	[user_id] [nvarchar](256) NULL,
	[stock_id] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[account_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[account_value]    Script Date: 2/13/2021 5:38:48 PM ******/
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
/****** Object:  Table [stockmarket].[location]    Script Date: 2/13/2021 5:38:48 PM ******/
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
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[user]    Script Date: 2/13/2021 5:38:48 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[user](
	[user_id] [nvarchar](256) NOT NULL,
	[email] [nvarchar](320) NULL
PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
ALTER TABLE [stockmarket].[account_value] ADD  DEFAULT (getdate()) FOR [valid_from]
GO
ALTER TABLE [stockmarket].[account]  WITH CHECK ADD FOREIGN KEY([stock_id])
REFERENCES [stockmarket].[stock] ([stock_id])
GO
ALTER TABLE [stockmarket].[account_value]  WITH CHECK ADD FOREIGN KEY([account_id])
REFERENCES [stockmarket].[account] ([account_id])
GO
ALTER TABLE [stockmarket].[location]  WITH CHECK ADD FOREIGN KEY([country_id])
REFERENCES [stockmarket].[country] ([country_id])
GO
ALTER TABLE [stockmarket].[location]  WITH CHECK ADD FOREIGN KEY([country_id])
REFERENCES [stockmarket].[country] ([country_id])
GO
ALTER TABLE [stockmarket].[location]  WITH CHECK ADD FOREIGN KEY([state_id])
REFERENCES [stockmarket].[state] ([state_id])
GO
ALTER TABLE [stockmarket].[location]  WITH CHECK ADD FOREIGN KEY([state_id])
REFERENCES [stockmarket].[state] ([state_id])
GO