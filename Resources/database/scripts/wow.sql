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

--
-- Name: __EFMigrationsHistory; Type: TABLE; Schema: public; Owner: plkn
--

CREATE TABLE public."__EFMigrationsHistory" (
    migration_id character varying(150) NOT NULL,
    product_version character varying(32) NOT NULL
);


ALTER TABLE public."__EFMigrationsHistory" OWNER TO plkn;

--
-- Name: category_dev_schedule; Type: TABLE; Schema: public; Owner: plkn
--

CREATE TABLE public.category_dev_schedule (
    id integer NOT NULL,
    hob character varying(40) NOT NULL,
    mm character varying(40) NOT NULL,
    cm_buyer text NOT NULL,
    sub_cat_name text NOT NULL,
    review_type text NOT NULL,
    sub_date_foodco_products date,
    notice_of_probable_delisting date,
    suppliers_engagement date,
    final_submission_for_branded date,
    info_of_new_and_deleted_lines date,
    provide_all_wnas_waf_wpf_to_buyer date,
    visual_planogram_due_to_stores date NOT NULL,
    date_added date DEFAULT CURRENT_DATE NOT NULL
);


ALTER TABLE public.category_dev_schedule OWNER TO plkn;

--
-- Name: category_dev_schedule_id_seq; Type: SEQUENCE; Schema: public; Owner: plkn
--

CREATE SEQUENCE public.category_dev_schedule_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.category_dev_schedule_id_seq OWNER TO plkn;

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
