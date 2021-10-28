EdmKey,PortKeym,LocKey
/
CREATE TABLE PortLoc (
    EdmKey INTEGER,
    PortKey INTEGER,
    PortNum TEXT ENCODING DICT(32),
    PortName TEXT ENCODING DICT(32),
    LocKey INTEGER
);
/
CREATE TABLE Program_EDM (
    EdmKey INTEGER,
    ProgramKey INTEGER,
    ProgramReference TEXT ENCODING DICT(32),
    ProgramName TEXT ENCODING DICT(32),
    PricingProgramId TEXT ENCODING DICT(32),
    PortKey INTEGER,
    PerilKey INTEGER,
    ProgramStatus TEXT ENCODING DICT(32),
    ProgramInceptionDate TIMESTAMP(0),
    ProgramExpiryDate TIMESTAMP(0),
    IsLiveData TINYINT
);
/
CREATE TABLE ExpDataEQ (
    EdmKey INTEGER,
    EdmName TEXT ENCODING DICT(16),
    EdmStatus TEXT ENCODING DICT(8),
    EDMYear SMALLINT,
    FactLocPerilId BIGINT,
    AccGrpName TEXT ENCODING DICT(32),
    AccGrpNum TEXT ENCODING DICT(32),
    ConstructionCategory TEXT ENCODING DICT(8),
    Construction TEXT ENCODING DICT(16),
    OccupancyCategory TEXT ENCODING DICT(8),
    Occupancy TEXT ENCODING DICT(16),
    OccupancySubCategory TEXT ENCODING DICT(8),
    YearBand TEXT ENCODING DICT(8),
    FloorAreaBand TEXT ENCODING DICT(8),
    NumStoryBand TEXT ENCODING DICT(8),
    COUNTRYNAME TEXT ENCODING DICT(16),
    STATECODE TEXT ENCODING DICT(16),
    STATENAME TEXT ENCODING DICT(16),
    CITY TEXT ENCODING DICT(32),
    COUNTY TEXT ENCODING DICT(32),
    POSTALCODE TEXT ENCODING DICT(32),
    GeoResDescription TEXT ENCODING DICT(8),
    LATITUDE DECIMAL(9, 6) ENCODING FIXED(32),
    LONGITUDE DECIMAL(9, 6) ENCODING FIXED(32),
    LocKey BIGINT,
    LocName TEXT ENCODING DICT(32),
    SiteName TEXT ENCODING DICT(32),
    LocNum TEXT ENCODING DICT(32),
    NUMBLDGS INTEGER,
    PerilName TEXT ENCODING DICT(8),
    CedantName TEXT ENCODING DICT(16),
    BrokerName TEXT ENCODING DICT(16),
    UnderwriterName TEXT ENCODING DICT(16),
    PortName TEXT ENCODING DICT(16),
    LandSlide TEXT ENCODING DICT(8),
    Liquefaction TEXT ENCODING DICT(8),
    SoilType TEXT ENCODING DICT(8),
    SoftStory TEXT ENCODING DICT(8),
    Cladding TEXT ENCODING DICT(8),
    BuildingExt TEXT ENCODING DICT(8),
    Ornament TEXT ENCODING DICT(8),
    ConstQualityEQ TEXT ENCODING DICT(8),
    EngFoundation TEXT ENCODING DICT(8),
    FrameBolt TEXT ENCODING DICT(8),
    TiltUpRetro TEXT ENCODING DICT(8),
    URMRetro TEXT ENCODING DICT(8),
    TIV DOUBLE,
    COUNTRYCODE TEXT ENCODING DICT(16),
    COUNTYCODE TEXT ENCODING DICT(16),
    ExposedLimit DOUBLE
);