CREATE TABLE pools (
    id INTEGER,
    name BLOB,
    created_at datetime,
    updated_at datetime,
    creator_id INTEGER,
    description BLOB,
    constraint pools_pk primary key (id)
);

CREATE TABLE posts (
    id INTEGER,
    uploader_id INTEGER,
    created_at datetime,
    md5 BLOB,
    source BLOB,
    rating BLOB,
    image_width INTEGER,
    image_height INTEGER,
    tag_string BLOB,
    locked_tags BLOB,
    fav_count INTEGER,
    file_ext BLOB,
    parent_id INTEGER,
    change_seq INTEGER,
    approver_id INTEGER,
    file_size INTEGER,
    comment_count INTEGER,
    description BLOB,
    duration DECIMAL,
    updated_at datetime,
    is_deleted BLOB,
    is_pending BLOB,
    is_flagged BLOB,
    score INTEGER,
    up_score INTEGER,
    down_score INTEGER,
    is_rating_locked BLOB,
    is_status_locked BLOB,
    is_note_locked BLOB,
    constraint posts_pk primary key (id)
);

CREATE TABLE aliases (
    id INTEGER,
    antecedent_name BLOB,
    consequent_name BLOB,
    created_at datetime,
    status BLOB,
    constraint aliases_pk primary key (id)
);

CREATE TABLE implications (
    id INTEGER,
    antecedent_name BLOB,
    consequent_name BLOB,
    created_at datetime,
    status BLOB,
    constraint implications_pk primary key (id)
);

CREATE TABLE wikis (
    id INTEGER,
    created_at datetime,
    updated_at datetime,
    title BLOB,
    body BLOB,
    creator_id INTEGER,
    updater_id INTEGER,
    is_locked BLOB,
    constraint wikis_id primary key (id)
);

CREATE INDEX aliases_ant on aliases (antecedent_name);
CREATE INDEX aliases_con on aliases (consequent_name);
CREATE INDEX implications_ant on implications (antecedent_name);
CREATE INDEX implications_con on implications (consequent_name);
CREATE INDEX wikis_title on wikis (title);