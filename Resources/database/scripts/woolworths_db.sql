
CREATE DATABASE woolworths_db WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'en_AU.UTF-8' LC_CTYPE = 'en_AU.UTF-8';


ALTER DATABASE woolworths_db OWNER TO plkn;

\connect woolworths_db

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;





CREATE TABLE IF NOT EXISTS "__EFMigrationsHistory" (
    migration_id character varying(150) NOT NULL,
    product_version character varying(32) NOT NULL,
    CONSTRAINT pk___ef_migrations_history PRIMARY KEY (migration_id)
);

ALTER TABLE public."__EFMigrationsHistory" OWNER TO plkn;

CREATE TABLE category_dev_schedule (
    id serial NOT NULL,
    hob character varying(40) NOT NULL,
    mm character varying(40) NOT NULL,
    cm_buyer text NOT NULL,
    sub_cat_name text NOT NULL,
    review_type text NOT NULL,
    sub_date_foodco_products date NULL,
    notice_of_probable_delisting date NULL,
    suppliers_engagement date NULL,
    final_submission_for_branded date NULL,
    info_of_new_and_deleted_lines date NULL,
    provide_all_wnas_waf_wpf_to_buyer date NULL,
    visual_planogram_due_to_stores date NOT NULL,
    date_added date NOT NULL DEFAULT (current_date),
    CONSTRAINT pk_woolworths PRIMARY KEY (id)
);


ALTER TABLE public.category_dev_schedule OWNER TO plkn;






--
-- Name: category_dev_schedule_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: plkn
--

ALTER SEQUENCE public.category_dev_schedule_id_seq OWNED BY public.category_dev_schedule.id;


--
-- Name: category_dev_schedule id; Type: DEFAULT; Schema: public; Owner: plkn
--

ALTER TABLE ONLY public.category_dev_schedule ALTER COLUMN id SET DEFAULT nextval('public.category_dev_schedule_id_seq'::regclass);


--
-- Name: __EFMigrationsHistory pk___ef_migrations_history; Type: CONSTRAINT; Schema: public; Owner: plkn
--

ALTER TABLE ONLY public."__EFMigrationsHistory"
    ADD CONSTRAINT pk___ef_migrations_history PRIMARY KEY (migration_id);


--
-- Name: category_dev_schedule pk_woolworths; Type: CONSTRAINT; Schema: public; Owner: plkn
--

ALTER TABLE ONLY public.category_dev_schedule
    ADD CONSTRAINT pk_woolworths PRIMARY KEY (id);





INSERT INTO "__EFMigrationsHistory" (migration_id, product_version)
VALUES ('20200511040558_Added timestamp', '3.1.3');
