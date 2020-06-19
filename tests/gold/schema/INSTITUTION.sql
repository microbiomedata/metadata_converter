--------------------------------------------------------
--  DDL for Table INSTITUTION
--------------------------------------------------------

  CREATE TABLE "GOLD"."INSTITUTION" 
   (	"ID" NUMBER, 
	"NAME" VARCHAR2(512 BYTE), 
	"URL" VARCHAR2(500 BYTE), 
	"COUNTRY" VARCHAR2(100 BYTE), 
	"ORGANIZATION" VARCHAR2(200 BYTE), 
	"DEPARTMENT" VARCHAR2(200 BYTE), 
	"LABORATORY" VARCHAR2(200 BYTE), 
	"IS_CURATED" VARCHAR2(3 BYTE) DEFAULT 'No'
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;