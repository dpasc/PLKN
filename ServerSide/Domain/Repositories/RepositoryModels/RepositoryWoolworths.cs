using Domain.Data.EntityFrameworkModels.Contexts;
using Domain.Data.EntityFrameworkModels.Models;
using Domain.Repositories.RepositoryModels;

namespace Domain.Repositories{

    public class RepositoryWoolworths : RepositoryMain<Woolworths,ContextWoolworths>
    {
        public RepositoryWoolworths(ContextWoolworths context):base(context)
        {
            
        }

    }


}