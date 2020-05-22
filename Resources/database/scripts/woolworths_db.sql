CREATE TABLE IF NOT EXISTS "__EFMigrationsHistory" (
    migration_id character varying(150) NOT NULL,
    product_version character varying(32) NOT NULL,
    CONSTRAINT pk___ef_migrations_history PRIMARY KEY (migration_id)
);

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

INSERT INTO "__EFMigrationsHistory" (migration_id, product_version)
VALUES ('20200511040558_Added timestamp', '3.1.3');
