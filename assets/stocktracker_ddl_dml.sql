USE [STS]
GO
/****** Object:  Schema [stockmarket]    Script Date: 2/28/2021 7:41:48 PM ******/
CREATE SCHEMA [stockmarket]
GO
/****** Object:  Table [stockmarket].[account]    Script Date: 2/28/2021 7:41:48 PM ******/
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
/****** Object:  Table [stockmarket].[account_value]    Script Date: 2/28/2021 7:41:49 PM ******/
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
/****** Object:  Table [stockmarket].[country]    Script Date: 2/28/2021 7:41:49 PM ******/
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
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[location]    Script Date: 2/28/2021 7:41:49 PM ******/
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
/****** Object:  Table [stockmarket].[state]    Script Date: 2/28/2021 7:41:49 PM ******/
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
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [stockmarket].[stock]    Script Date: 2/28/2021 7:41:49 PM ******/
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
/****** Object:  Table [stockmarket].[user]    Script Date: 2/28/2021 7:41:49 PM ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [stockmarket].[user](
	[user_id] [nvarchar](256) NOT NULL,
	[email] [nvarchar](320) NULL,
PRIMARY KEY CLUSTERED 
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]
GO
SET IDENTITY_INSERT [stockmarket].[country] ON 
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (2, N'Afghanistan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (3, N'Albania')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (4, N'Algeria')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (5, N'American Samoa')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (6, N'Andorra')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (7, N'Angola')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (8, N'Anguilla')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (9, N'Antarctica')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (10, N'Antigua and Barbuda')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (11, N'Argentina')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (12, N'Armenia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (13, N'Aruba')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (14, N'Australia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (15, N'Austria')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (16, N'Azerbaijan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (17, N'Bahamas')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (18, N'Bahrain')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (19, N'Bangladesh')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (20, N'Barbados')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (21, N'Belarus')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (22, N'Belgium')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (23, N'Belize')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (24, N'Benin')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (25, N'Bermuda')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (26, N'Bhutan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (27, N'Bolivia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (28, N'Bosnia and Herzegovina')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (29, N'Botswana')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (30, N'Bouvet Island')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (31, N'Brazil')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (32, N'British Indian Ocean Territory')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (33, N'Brunei Darussalam')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (34, N'Bulgaria')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (35, N'Burkina Faso')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (36, N'Burundi')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (37, N'Cambodia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (38, N'Cameroon')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (39, N'Canada')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (40, N'Cape Verde')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (41, N'Cayman Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (42, N'Central African Republic')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (43, N'Chad')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (44, N'Chile')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (45, N'China')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (46, N'Christmas Island')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (47, N'Cocos (Keeling) Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (48, N'Colombia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (49, N'Comoros')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (50, N'Democratic Republic of the Congo')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (51, N'Republic of Congo')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (52, N'Cook Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (53, N'Costa Rica')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (54, N'Croatia (Hrvatska)')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (55, N'Cuba')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (56, N'Cyprus')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (57, N'Czech Republic')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (58, N'Denmark')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (59, N'Djibouti')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (60, N'Dominica')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (61, N'Dominican Republic')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (62, N'East Timor')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (63, N'Ecuador')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (64, N'Egypt')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (65, N'El Salvador')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (66, N'Equatorial Guinea')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (67, N'Eritrea')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (68, N'Estonia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (69, N'Ethiopia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (70, N'Falkland Islands (Malvinas)')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (71, N'Faroe Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (72, N'Fiji')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (73, N'Finland')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (74, N'France')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (75, N'France, Metropolitan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (76, N'French Guiana')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (77, N'French Polynesia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (78, N'French Southern Territories')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (79, N'Gabon')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (80, N'Gambia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (81, N'Georgia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (82, N'Germany')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (83, N'Ghana')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (84, N'Gibraltar')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (85, N'Guernsey')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (86, N'Greece')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (87, N'Greenland')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (88, N'Grenada')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (89, N'Guadeloupe')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (90, N'Guam')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (91, N'Guatemala')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (92, N'Guinea')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (93, N'Guinea-Bissau')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (94, N'Guyana')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (95, N'Haiti')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (96, N'Heard and Mc Donald Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (97, N'Honduras')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (98, N'Hong Kong')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (99, N'Hungary')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (100, N'Iceland')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (101, N'India')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (102, N'Isle of Man')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (103, N'Indonesia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (104, N'Iran (Islamic Republic of)')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (105, N'Iraq')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (106, N'Ireland')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (107, N'Israel')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (108, N'Italy')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (109, N'Ivory Coast')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (110, N'Jersey')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (111, N'Jamaica')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (112, N'Japan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (113, N'Jordan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (114, N'Kazakhstan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (115, N'Kenya')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (116, N'Kiribati')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (117, N'Korea, Democratic People''s Republic of')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (118, N'Korea, Republic of')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (119, N'Kosovo')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (120, N'Kuwait')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (121, N'Kyrgyzstan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (122, N'Lao People''s Democratic Republic')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (123, N'Latvia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (124, N'Lebanon')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (125, N'Lesotho')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (126, N'Liberia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (127, N'Libyan Arab Jamahiriya')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (128, N'Liechtenstein')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (129, N'Lithuania')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (130, N'Luxembourg')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (131, N'Macau')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (132, N'North Macedonia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (133, N'Madagascar')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (134, N'Malawi')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (135, N'Malaysia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (136, N'Maldives')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (137, N'Mali')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (138, N'Malta')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (139, N'Marshall Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (140, N'Martinique')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (141, N'Mauritania')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (142, N'Mauritius')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (143, N'Mayotte')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (144, N'Mexico')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (145, N'Micronesia, Federated States of')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (146, N'Moldova, Republic of')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (147, N'Monaco')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (148, N'Mongolia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (149, N'Montenegro')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (150, N'Montserrat')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (151, N'Morocco')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (152, N'Mozambique')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (153, N'Myanmar')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (154, N'Namibia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (155, N'Nauru')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (156, N'Nepal')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (157, N'Netherlands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (158, N'Netherlands Antilles')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (159, N'New Caledonia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (160, N'New Zealand')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (161, N'Nicaragua')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (162, N'Niger')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (163, N'Nigeria')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (164, N'Niue')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (165, N'Norfolk Island')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (166, N'Northern Mariana Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (167, N'Norway')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (168, N'Oman')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (169, N'Pakistan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (170, N'Palau')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (171, N'Palestine')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (172, N'Panama')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (173, N'Papua New Guinea')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (174, N'Paraguay')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (175, N'Peru')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (176, N'Philippines')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (177, N'Pitcairn')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (178, N'Poland')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (179, N'Portugal')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (180, N'Puerto Rico')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (181, N'Qatar')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (182, N'Reunion')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (183, N'Romania')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (184, N'Russian Federation')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (185, N'Rwanda')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (186, N'Saint Kitts and Nevis')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (187, N'Saint Lucia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (188, N'Saint Vincent and the Grenadines')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (189, N'Samoa')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (190, N'San Marino')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (191, N'Sao Tome and Principe')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (192, N'Saudi Arabia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (193, N'Senegal')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (194, N'Serbia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (195, N'Seychelles')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (196, N'Sierra Leone')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (197, N'Singapore')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (198, N'Slovakia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (199, N'Slovenia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (200, N'Solomon Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (201, N'Somalia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (202, N'South Africa')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (203, N'South Georgia South Sandwich Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (204, N'South Sudan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (205, N'Spain')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (206, N'Sri Lanka')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (207, N'St. Helena')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (208, N'St. Pierre and Miquelon')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (209, N'Sudan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (210, N'Suriname')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (211, N'Svalbard and Jan Mayen Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (212, N'Swaziland')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (213, N'Sweden')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (214, N'Switzerland')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (215, N'Syrian Arab Republic')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (216, N'Taiwan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (217, N'Tajikistan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (218, N'Tanzania, United Republic of')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (219, N'Thailand')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (220, N'Togo')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (221, N'Tokelau')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (222, N'Tonga')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (223, N'Trinidad and Tobago')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (224, N'Tunisia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (225, N'Turkey')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (226, N'Turkmenistan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (227, N'Turks and Caicos Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (228, N'Tuvalu')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (229, N'Uganda')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (230, N'Ukraine')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (231, N'United Arab Emirates')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (232, N'United Kingdom')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (233, N'United States')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (234, N'United States minor outlying islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (235, N'Uruguay')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (236, N'Uzbekistan')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (237, N'Vanuatu')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (238, N'Vatican City State')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (239, N'Venezuela')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (240, N'Vietnam')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (241, N'Virgin Islands (British)')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (242, N'Virgin Islands (U.S.)')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (243, N'Wallis and Futuna Islands')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (244, N'Western Sahara')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (245, N'Yemen')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (246, N'Zambia')
GO
INSERT [stockmarket].[country] ([country_id], [country_name]) VALUES (247, N'Zimbabwe')
GO
SET IDENTITY_INSERT [stockmarket].[country] OFF
GO
SET IDENTITY_INSERT [stockmarket].[state] ON 
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (2, N'District of Columbia')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (3, N'Alabama')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (4, N'Alaska')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (5, N'Arizona')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (6, N'Arkansas')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (7, N'California')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (8, N'Colorado')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (9, N'Connecticut')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (10, N'Delaware')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (11, N'Florida')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (12, N'Georgia')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (13, N'Hawaii')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (14, N'Idaho')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (15, N'Illinois')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (16, N'Indiana')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (17, N'Iowa')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (18, N'Kansas')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (19, N'Kentucky')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (20, N'Louisiana')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (21, N'Maine')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (22, N'Maryland')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (23, N'Massachusetts')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (24, N'Michigan')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (25, N'Minnesota')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (26, N'Mississippi')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (27, N'Missouri')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (28, N'Montana')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (29, N'Nebraska')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (30, N'Nevada')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (31, N'New Hampshire')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (32, N'New Jersey')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (33, N'New Mexico')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (34, N'New York')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (35, N'North Carolina')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (36, N'North Dakota')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (37, N'Ohio')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (38, N'Oklahoma')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (39, N'Oregon')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (40, N'Pennsylvania')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (41, N'Rhode Island')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (42, N'South Carolina')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (43, N'South Dakota')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (44, N'Tennessee')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (45, N'Texas')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (46, N'Utah')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (47, N'Vermont')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (48, N'Virginia')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (49, N'Washington')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (50, N'West Virginia')
GO
INSERT [stockmarket].[state] ([state_id], [state_name]) VALUES (51, N'Wisconsin')
GO
SET IDENTITY_INSERT [stockmarket].[state] OFF
GO
SET IDENTITY_INSERT [stockmarket].[stock] ON 
GO
INSERT [stockmarket].[stock] ([stock_id], [symbol]) VALUES (1, N'VOO')
GO
INSERT [stockmarket].[stock] ([stock_id], [symbol]) VALUES (2, N'TSLA')
GO
INSERT [stockmarket].[stock] ([stock_id], [symbol]) VALUES (3, N'GME')
GO
INSERT [stockmarket].[stock] ([stock_id], [symbol]) VALUES (4, N'GOOGL')
GO
SET IDENTITY_INSERT [stockmarket].[stock] OFF
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
