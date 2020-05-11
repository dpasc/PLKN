using System;
using System.Collections.Generic;
using System.Text;
using Domain.Repositories.RepoInterfaces;
using NodaTime;

namespace Domain.Data.EntityFrameworkModels.Models
{
    public class Woolworths : IEntity
    {
        public int Id { get; set; }
        public string HOB { get; set; }
        public string MM { get; set; }
        public string CMBuyer { get; set; }
        public string SubCategoryName { get; set; }
        //Minor or Major 
        public string TypeOfReview { get; set; }
        //Submission date for FoodCo Own Brand Products
        public LocalDate? SubDateForFoodCoOwnBrandProducts { get; set; }

        //"Notice of Probable Delisting" letter sent to impacted suppliers
        public LocalDate? NoticeOfProbableDelisting { get; set; }

        //Supplier engagement:
        //Submissions opened for review & Supplier recommendations for deletions

        public LocalDate? SuppliersEngagement { get; set; }

        //Final submission date for Branded Products
        public LocalDate? FinalSubmissionDateForBrandedProducts { get; set; }

        //Results to Suppliers of New & Deleted Lines
        //"Notice of Final Delisting" letter sent to impacted suppliers
        public LocalDate? InfoOfNewAndDeletedLines { get; set; }

        //Suppliers to provide all WNAS, WAF, WPF to Buyer
        public LocalDate? ProvideAllWnasWafWpfToBuyers { get; set; }

        //VISUAL PLANOGRAM DUE TO STORES
        public LocalDate VisualPlanogramDueToStores { get; set; }

        public LocalDate DateAdded {get; set;}

    }

}
