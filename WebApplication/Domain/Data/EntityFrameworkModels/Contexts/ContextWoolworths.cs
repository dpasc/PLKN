using Domain.Data.EntityFrameworkModels.Models;
using Microsoft.EntityFrameworkCore;
using Microsoft.Extensions.Configuration;
using System;
using System.Collections.Generic;
using System.Text;

namespace Domain.Data.EntityFrameworkModels.Contexts
{
    public class ContextWoolworths :DbContext
    {

       
        protected override void OnConfiguring(DbContextOptionsBuilder optionsBuilder)
        {
            optionsBuilder.UseNpgsql(@"HOST=localhost;DB=woolworths_db;UID=plkn;PWD=password;Port=5432;",
            o => o.UseNodaTime());
        }
        protected override void OnModelCreating(ModelBuilder mB)
        {
           
            mB.Entity<Woolworths>()
                 .Property(w => w.Id)
                 .IsRequired(true)
                 .UseSerialColumn()
                 .HasColumnName("id");

            mB.Entity<Woolworths>()
                .Property(w => w.HOB)
                .IsRequired(true)
                .HasMaxLength(40)
                .HasColumnName("hob");

            mB.Entity<Woolworths>()
                .Property(w => w.MM)
                .IsRequired(true)
                .HasMaxLength(40)
                .HasColumnName("mm");
          

            mB.Entity<Woolworths>()
                .Property(w => w.CMBuyer)
                .IsRequired(true)
                .HasColumnName("cm_buyer");

            mB.Entity<Woolworths>()
                .Property(w => w.SubCategoryName)
                .IsRequired(true)
                .HasColumnName("sub_cat_name");

            mB.Entity<Woolworths>()
                .Property(w => w.TypeOfReview)
                .IsRequired(true)
                .HasColumnName("review_type");

            mB.Entity<Woolworths>()
                .Property(w => w.SubDateForFoodCoOwnBrandProducts)
                .IsRequired(false)
                .HasColumnName("sub_date_foodco_products");

            mB.Entity<Woolworths>()
                .Property(w => w.NoticeOfProbableDelisting)
                .IsRequired(false)
                .HasColumnName("notice_of_probable_delisting");

            mB.Entity<Woolworths>()
                .Property(w => w.SuppliersEngagement)
                .IsRequired(false)
                .HasColumnName("suppliers_engagement");

            mB.Entity<Woolworths>()
                .Property(w => w.FinalSubmissionDateForBrandedProducts)
                .IsRequired(false)
                .HasColumnName("final_submission_for_branded");

            mB.Entity<Woolworths>()
                .Property(w => w.InfoOfNewAndDeletedLines)
                .IsRequired(false)
                .HasColumnName("info_of_new_and_deleted_lines");

            mB.Entity<Woolworths>()
                .Property(w => w.ProvideAllWnasWafWpfToBuyers)
                .IsRequired(false)
                .HasColumnName("provide_all_wnas_waf_wpf_to_buyer");

            mB.Entity<Woolworths>()
                .Property(w => w.VisualPlanogramDueToStores)
                .IsRequired(true)
                .HasColumnName("visual_planogram_due_to_stores");
        }


        public DbSet<Woolworths> Woolworths { get; set; }

    }
}
