
using System.Collections.Generic;
using System.Threading.Tasks;
using Domain.Repositories.RepoInterfaces;
using Microsoft.EntityFrameworkCore;



namespace Domain.Repositories.RepositoryModels
{

    public abstract class RepositoryMain<TEntity, TContext>: IRepository<TEntity>

    where TEntity : class, IEntity
    where TContext : DbContext
    {
        public TContext context;
        public RepositoryMain(TContext context)
        {
            this.context = context;
        }

        public virtual async Task<List<TEntity>> GetAllRecords()
        {
            return await context.Set<TEntity>().ToListAsync();
        }

    }

  


}