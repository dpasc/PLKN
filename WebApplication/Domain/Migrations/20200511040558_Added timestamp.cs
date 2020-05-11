using Microsoft.EntityFrameworkCore.Migrations;
using NodaTime;
using Npgsql.EntityFrameworkCore.PostgreSQL.Metadata;

namespace Domain.Migrations
{
    public partial class Addedtimestamp : Migration
    {
        protected override void Up(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.CreateTable(
                name: "category_dev_schedule",
                columns: table => new
                {
                    id = table.Column<int>(nullable: false)
                        .Annotation("Npgsql:ValueGenerationStrategy", NpgsqlValueGenerationStrategy.SerialColumn),
                    hob = table.Column<string>(maxLength: 40, nullable: false),
                    mm = table.Column<string>(maxLength: 40, nullable: false),
                    cm_buyer = table.Column<string>(nullable: false),
                    sub_cat_name = table.Column<string>(nullable: false),
                    review_type = table.Column<string>(nullable: false),
                    sub_date_foodco_products = table.Column<LocalDate>(nullable: true),
                    notice_of_probable_delisting = table.Column<LocalDate>(nullable: true),
                    suppliers_engagement = table.Column<LocalDate>(nullable: true),
                    final_submission_for_branded = table.Column<LocalDate>(nullable: true),
                    info_of_new_and_deleted_lines = table.Column<LocalDate>(nullable: true),
                    provide_all_wnas_waf_wpf_to_buyer = table.Column<LocalDate>(nullable: true),
                    visual_planogram_due_to_stores = table.Column<LocalDate>(nullable: false),
                    date_added = table.Column<LocalDate>(nullable: false, defaultValueSql: "current_date")
                },
                constraints: table =>
                {
                    table.PrimaryKey("pk_woolworths", x => x.id);
                });
        }

        protected override void Down(MigrationBuilder migrationBuilder)
        {
            migrationBuilder.DropTable(
                name: "category_dev_schedule");
        }
    }
}
