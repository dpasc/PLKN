using System;
using System.Collections.Generic;
using System.Text;

namespace Domain.Data.EntityFrameworkModels.Models
{
    public class Woolworths
    {
        public int Id { get; set; }
        public string HOB { get; set; }
        public string MM { get; set; }
        public string CMBuyer { get; set; }
        public string SubCategoryName { get; set; }
        //Minor or Major 
        public string TypeOfReview { get; set; }
        //Submission date for FoodCo Own Brand Products
        public DateTime? SubDateForFoodCoOwnBrandProducts { get; set; }

        //"Notice of Probable Delisting" letter sent to impacted suppliers
        public DateTime? NoticeOfProbableDelisting { get; set; }

        //Supplier engagement:
        //Submissions opened for review & Supplier recommendations for deletions

        public DateTime? SuppliersEngagement { get; set; }

        //Final submission date for Branded Products
        public DateTime? FinalSubmissionDateForBrandedProducts { get; set; }

        //Results to Suppliers of New & Deleted Lines
        //"Notice of Final Delisting" letter sent to impacted suppliers
        public DateTime? InfoOfNewAndDeletedLines { get; set; }

        //Suppliers to provide all WNAS, WAF, WPF to Buyer
        public DateTime? ProvideAllWnasWafWpfToBuyers { get; set; }

        //VISUAL PLANOGRAM DUE TO STORES
        public DateTime VisualPlanogramDueToStores { get; set; }

    }

}
