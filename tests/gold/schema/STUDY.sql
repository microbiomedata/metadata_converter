--------------------------------------------------------
--  DDL for Table STUDY
--------------------------------------------------------

  CREATE TABLE "GOLD"."STUDY" 
   (	"STUDY_ID" NUMBER, 
	"STUDY_NAME" VARCHAR2(3000 BYTE), 
	"ITS_PROPOSAL_ID" NUMBER, 
	"NCBI_PROJECT_ID" NUMBER, 
	"ADD_DATE" TIMESTAMP (6), 
	"MOD_DATE" TIMESTAMP (6), 
	"CONTACT_ID" NUMBER, 
	"LAST_MOD_BY" NUMBER, 
	"IS_PUBLIC" VARCHAR2(24 BYTE), 
	"GPTS_PROPOSAL_ID" NUMBER, 
	"PROJECT_OID" NUMBER(*,0), 
	"ACTIVE" VARCHAR2(3 BYTE) DEFAULT 'Yes', 
	"LEGACY_GOLD_ID" VARCHAR2(9 BYTE), 
	"BIOPROJECT_NAME" VARCHAR2(2000 BYTE), 
	"GOLD_STUDY_NAME" VARCHAR2(4000 BYTE), 
	"DESCRIPTION" VARCHAR2(4000 BYTE), 
	"GOLD_ID" VARCHAR2(9 BYTE), 
	"METAGENOMIC" VARCHAR2(20 BYTE) DEFAULT 'No', 
	"STUDY_TYPE_ID" NUMBER(*,0) DEFAULT 2, 
	"ECOSYSTEM" VARCHAR2(1000 BYTE), 
	"ECOSYSTEM_CATEGORY" VARCHAR2(1000 BYTE), 
	"ECOSYSTEM_TYPE" VARCHAR2(1000 BYTE), 
	"ECOSYSTEM_SUBTYPE" VARCHAR2(1000 BYTE), 
	"SPECIFIC_ECOSYSTEM" VARCHAR2(1000 BYTE), 
	"OWNER_ID" NUMBER, 
	"IS_DRAFT" VARCHAR2(3 BYTE) DEFAULT 'No', 
	"PUBLIC_SP_COUNT" NUMBER DEFAULT 0, 
	"ADMIN_SP_COUNT" NUMBER DEFAULT 0, 
	"PUBLIC_AP_COUNT" NUMBER DEFAULT 0, 
	"ADMIN_AP_COUNT" NUMBER DEFAULT 0, 
	"PUBLIC_DAP_COUNT" NUMBER DEFAULT 0, 
	"ADMIN_DAP_COUNT" NUMBER DEFAULT 0, 
	"PUBLIC_BIOSAMPLE_COUNT" NUMBER DEFAULT 0, 
	"ADMIN_BIOSAMPLE_COUNT" NUMBER DEFAULT 0, 
	"IS_GEBA" VARCHAR2(5 BYTE) DEFAULT 'No', 
	"IS_HMP" VARCHAR2(5 BYTE) DEFAULT 'No', 
	"ECOSYSTEM_PATH_ID" NUMBER, 
	"IS_TEST" VARCHAR2(100 BYTE) DEFAULT 'No'
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 
 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1
  BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
