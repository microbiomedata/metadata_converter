--------------------------------------------------------
--  DDL for Table PUBLICATION
--------------------------------------------------------

  CREATE TABLE "GOLD"."PUBLICATION" 
   (	"PUBLICATION_ID" NUMBER(*,0), 
	"DOI" VARCHAR2(128 BYTE), 
	"PUBMED_ID" NUMBER(*,0), 
	"JOURNAL_ID" NUMBER(*,0), 
	"PUBMODEL" VARCHAR2(128 BYTE), 
	"VOLUME" VARCHAR2(128 BYTE), 
	"ISSUE" VARCHAR2(128 BYTE), 
	"PAGE" VARCHAR2(128 BYTE), 
	"PUBLICATION_DATE" DATE, 
	"ABSTRACT" VARCHAR2(3000 BYTE), 
	"AFFILIATION" VARCHAR2(4000 BYTE), 
	"TITLE" VARCHAR2(1000 BYTE), 
	"LAST_AUTHOR_ID" NUMBER(*,0), 
	"FIRST_AUTHOR_ID" NUMBER(*,0)
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
