drop table if exists blacklisted cascade;
drop table if exists favorited cascade;
drop table if exists implies cascade;
drop table if exists in_pool cascade;
drop table if exists is_tagged cascade;
drop table if exists pool cascade;
drop table if exists post cascade;
drop table if exists post_score cascade;
drop table if exists role cascade;
drop table if exists tag cascade;
drop table if exists text_post cascade;
drop table if exists text_post_score cascade;
drop table if exists "user" cascade;
drop table if exists wiki cascade;


create table blacklisted (
  tag text not null,
  "user" integer not null
);

create table favorited (
  "user" integer not null,
  post integer not null
);

create table implies (
  tag text not null,
  implies text not null
);

create table in_pool (
  pool integer not null,
  post integer not null,
  order_in_pool integer not null
);

create table is_tagged (
  post integer not null,
  tag text not null,
  is_example boolean not null default false
);

create table pool (
  id integer unique not null,
  name text not null,
  description text
);

create table post (
  id integer unique not null,
  file text unique not null,
  upload_date timestamp without time zone not null,
  uploader integer not null,
  parent integer,
  rating text not null,
  verified_by integer
);

create table post_score (
  "user" integer not null,
  post integer not null,
  is_like boolean not null
);

create table role (
  name text not null,
  can_verify boolean not null
);

create table tag (
  name text not null
);

create table text_post (
  id integer not null,
  "user" integer not null,
  content text not null,
  post integer
);

create table text_post_score (
  "user" integer not null,
  text_post integer not null,
  is_like boolean not null
);

create table "user" (
  id integer not null,
  username text unique not null,
  password_hash text not null,
  role text not null default 'Member'
);

create table wiki (
  tag text not null,
  content text not null
);




alter table blacklisted
    add constraint bl_pk primary key (tag, "user");
alter table favorited
    add constraint fa_pk primary key ("user", post);
alter table implies
    add constraint im_pk primary key (tag, implies);
alter table in_pool
    add constraint ip_pk primary key (pool, post);
alter table is_tagged
    add constraint it_pk primary key (post, tag);
alter table pool
    add constraint oo_pk primary key (id);
alter table post
    add constraint po_pk primary key (id);
alter table post_score
    add constraint ps_pk primary key ("user", post);
alter table role
    add constraint ro_pk primary key (name);
alter table tag
    add constraint ta_pk primary key (name);
alter table text_post
    add constraint tp_pk primary key (id);
alter table text_post_score
    add constraint ts_pk primary key ("user", text_post);
alter table "user"
    add constraint us_pk primary key (id);
alter table wiki
    add constraint wi_pk primary key (tag);

alter table blacklisted
    add constraint bl_fk_tag FOREIGN KEY (tag) references tag (name) on delete restrict;
alter table blacklisted
    add constraint bl_fk_user foreign key ("user") references "user" (id) on delete restrict;

alter table favorited
    add constraint fa_fk_user foreign key ("user") references "user" (id) on delete restrict;
alter table favorited
    add constraint fa_fk_post foreign key (post) references post (id) on delete restrict;

alter table implies
    add constraint im_fk_tag foreign key (tag) references tag (name) on delete restrict;
alter table implies
    add constraint im_fk_implies foreign key (implies) references tag (name) on delete restrict;

alter table in_pool
    add constraint ip_fk_pool foreign key (pool) references pool (id) on delete restrict;
alter table in_pool
    add constraint ip_fk_post foreign key (post) references post (id) on delete restrict;
alter table in_pool add constraint ip_uq_pool_order unique (pool, order_in_pool);

alter table is_tagged
    add constraint it_fk_post foreign key (post) references post (id) on delete restrict;
alter table is_tagged
    add constraint it_fk_tag foreign key (tag) references tag (name) on delete restrict;
-- todo: IC8: post can only be an example of existing wikis

-- pool needs no other constraints

alter table post
    add constraint po_fk_uploader foreign key (uploader) references "user" (id) on delete restrict;
alter table post
    add constraint po_fk_verified_by foreign key (verified_by) references "user" (id) on delete restrict;
alter table post
    add constraint po_fk_parent foreign key (parent) references post (id) on delete restrict;
alter table post add constraint ic3 check ( parent != id );

-- todo: IC6: only users with a privileged role may verify a post

alter table post_score
    add constraint ps_fk_user foreign key ("user") references "user" (id) on delete restrict;
alter table post_score
    add constraint ps_fk_post foreign key (post) references post (id) on delete restrict;

-- role needs no other constraints

alter table text_post
    add constraint tp_fk_user foreign key ("user") references "user" (id) on delete restrict;
alter table text_post
    add constraint tp_fk_post foreign key (post) references post (id) on delete restrict;

alter table text_post_score
    add constraint ts_fk_user foreign key ("user") references "user" (id) on delete restrict;
alter table text_post_score
    add constraint ts_fk_text_post foreign key (text_post) references text_post (id) on delete restrict;

alter table "user"
    add constraint us_fk_role foreign key (role) references role (name) on delete restrict;

alter table wiki
    add constraint wi_fk_tag foreign key (tag) references tag (name) on delete restrict;
-- todo: add ic8 trigger
