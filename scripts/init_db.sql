-- ====================================
-- Credit Risk Scoring Project
-- Database Initialization Script
-- ====================================

-- Create schema
CREATE SCHEMA IF NOT EXISTS credit_risk;

-- Set search path
SET search_path TO credit_risk, public;

-- ====================================
-- Main Application Table
-- ====================================
CREATE TABLE IF NOT EXISTS application_train (
    SK_ID_CURR INTEGER PRIMARY KEY,
    TARGET INTEGER,
    NAME_CONTRACT_TYPE VARCHAR(50),
    CODE_GENDER VARCHAR(10),
    FLAG_OWN_CAR VARCHAR(5),
    FLAG_OWN_REALTY VARCHAR(5),
    CNT_CHILDREN INTEGER,
    AMT_INCOME_TOTAL DECIMAL(15,2),
    AMT_CREDIT DECIMAL(15,2),
    AMT_ANNUITY DECIMAL(15,2),
    AMT_GOODS_PRICE DECIMAL(15,2),
    NAME_TYPE_SUITE VARCHAR(50),
    NAME_INCOME_TYPE VARCHAR(50),
    NAME_EDUCATION_TYPE VARCHAR(50),
    NAME_FAMILY_STATUS VARCHAR(50),
    NAME_HOUSING_TYPE VARCHAR(50),
    REGION_POPULATION_RELATIVE DECIMAL(10,6),
    DAYS_BIRTH INTEGER,
    DAYS_EMPLOYED INTEGER,
    DAYS_REGISTRATION DECIMAL(15,2),
    DAYS_ID_PUBLISH INTEGER,
    OWN_CAR_AGE DECIMAL(10,2),
    FLAG_MOBIL INTEGER,
    FLAG_EMP_PHONE INTEGER,
    FLAG_WORK_PHONE INTEGER,
    FLAG_CONT_MOBILE INTEGER,
    FLAG_PHONE INTEGER,
    FLAG_EMAIL INTEGER,
    OCCUPATION_TYPE VARCHAR(50),
    CNT_FAM_MEMBERS DECIMAL(10,2),
    REGION_RATING_CLIENT INTEGER,
    REGION_RATING_CLIENT_W_CITY INTEGER,
    WEEKDAY_APPR_PROCESS_START VARCHAR(20),
    HOUR_APPR_PROCESS_START INTEGER,
    REG_REGION_NOT_LIVE_REGION INTEGER,
    REG_REGION_NOT_WORK_REGION INTEGER,
    LIVE_REGION_NOT_WORK_REGION INTEGER,
    REG_CITY_NOT_LIVE_CITY INTEGER,
    REG_CITY_NOT_WORK_CITY INTEGER,
    LIVE_CITY_NOT_WORK_CITY INTEGER,
    ORGANIZATION_TYPE VARCHAR(100),
    -- Additional columns will be added during data loading
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ====================================
-- Bureau Table (Credit history from other institutions)
-- ====================================
CREATE TABLE IF NOT EXISTS bureau (
    SK_ID_BUREAU INTEGER PRIMARY KEY,
    SK_ID_CURR INTEGER,
    CREDIT_ACTIVE VARCHAR(20),
    CREDIT_CURRENCY VARCHAR(20),
    DAYS_CREDIT INTEGER,
    CREDIT_DAY_OVERDUE INTEGER,
    DAYS_CREDIT_ENDDATE DECIMAL(15,2),
    DAYS_ENDDATE_FACT DECIMAL(15,2),
    AMT_CREDIT_MAX_OVERDUE DECIMAL(15,2),
    CNT_CREDIT_PROLONG INTEGER,
    AMT_CREDIT_SUM DECIMAL(15,2),
    AMT_CREDIT_SUM_DEBT DECIMAL(15,2),
    AMT_CREDIT_SUM_LIMIT DECIMAL(15,2),
    AMT_CREDIT_SUM_OVERDUE DECIMAL(15,2),
    CREDIT_TYPE VARCHAR(50),
    DAYS_CREDIT_UPDATE INTEGER,
    AMT_ANNUITY DECIMAL(15,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ====================================
-- Bureau Balance Table
-- ====================================
CREATE TABLE IF NOT EXISTS bureau_balance (
    id SERIAL PRIMARY KEY,
    SK_ID_BUREAU INTEGER,
    MONTHS_BALANCE INTEGER,
    STATUS VARCHAR(5),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ====================================
-- Previous Application Table
-- ====================================
CREATE TABLE IF NOT EXISTS previous_application (
    SK_ID_PREV INTEGER PRIMARY KEY,
    SK_ID_CURR INTEGER,
    NAME_CONTRACT_TYPE VARCHAR(50),
    AMT_ANNUITY DECIMAL(15,2),
    AMT_APPLICATION DECIMAL(15,2),
    AMT_CREDIT DECIMAL(15,2),
    AMT_DOWN_PAYMENT DECIMAL(15,2),
    AMT_GOODS_PRICE DECIMAL(15,2),
    WEEKDAY_APPR_PROCESS_START VARCHAR(20),
    HOUR_APPR_PROCESS_START INTEGER,
    FLAG_LAST_APPL_PER_CONTRACT VARCHAR(5),
    NFLAG_LAST_APPL_IN_DAY INTEGER,
    NAME_CASH_LOAN_PURPOSE VARCHAR(50),
    NAME_CONTRACT_STATUS VARCHAR(50),
    DAYS_DECISION INTEGER,
    NAME_PAYMENT_TYPE VARCHAR(50),
    CODE_REJECT_REASON VARCHAR(50),
    NAME_TYPE_SUITE VARCHAR(50),
    NAME_CLIENT_TYPE VARCHAR(20),
    NAME_GOODS_CATEGORY VARCHAR(50),
    NAME_PORTFOLIO VARCHAR(20),
    NAME_PRODUCT_TYPE VARCHAR(20),
    CHANNEL_TYPE VARCHAR(50),
    SELLERPLACE_AREA INTEGER,
    NAME_SELLER_INDUSTRY VARCHAR(50),
    CNT_PAYMENT DECIMAL(10,2),
    NAME_YIELD_GROUP VARCHAR(20),
    PRODUCT_COMBINATION VARCHAR(50),
    DAYS_FIRST_DRAWING DECIMAL(15,2),
    DAYS_FIRST_DUE DECIMAL(15,2),
    DAYS_LAST_DUE_1ST_VERSION DECIMAL(15,2),
    DAYS_LAST_DUE DECIMAL(15,2),
    DAYS_TERMINATION DECIMAL(15,2),
    NFLAG_INSURED_ON_APPROVAL DECIMAL(10,2),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ====================================
-- Indexes for better query performance
-- ====================================
CREATE INDEX IF NOT EXISTS idx_application_target ON application_train(TARGET);
CREATE INDEX IF NOT EXISTS idx_bureau_sk_id_curr ON bureau(SK_ID_CURR);
CREATE INDEX IF NOT EXISTS idx_bureau_balance_sk_id_bureau ON bureau_balance(SK_ID_BUREAU);
CREATE INDEX IF NOT EXISTS idx_previous_application_sk_id_curr ON previous_application(SK_ID_CURR);

-- ====================================
-- Features Table (for storing engineered features)
-- ====================================
CREATE TABLE IF NOT EXISTS features (
    SK_ID_CURR INTEGER PRIMARY KEY,
    feature_vector JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ====================================
-- Predictions Table (for storing model predictions)
-- ====================================
CREATE TABLE IF NOT EXISTS predictions (
    id SERIAL PRIMARY KEY,
    SK_ID_CURR INTEGER,
    probability DECIMAL(10,6),
    score INTEGER,
    decision VARCHAR(20),
    model_version VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX IF NOT EXISTS idx_predictions_sk_id_curr ON predictions(SK_ID_CURR);
CREATE INDEX IF NOT EXISTS idx_predictions_created_at ON predictions(created_at);

-- ====================================
-- Grant permissions
-- ====================================
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA credit_risk TO credit_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA credit_risk TO credit_user;

-- Log completion
DO $$
BEGIN
    RAISE NOTICE 'Database initialization completed successfully!';
END $$;
