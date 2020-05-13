using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;
using Microsoft.Extensions.Logging;
using Domain.Repositories.RepoInterfaces;
using Domain.Repositories.RepositoryModels;

namespace API.Controllers
{
    [ApiController]
    [Route("api/[controller]")]
    public abstract class ControllerMain<TEntity,TRepository> : ControllerBase
        where TEntity :class, IEntity 
        where TRepository : IRepository<TEntity>
    {

        internal readonly TRepository _repository;

        public ControllerMain(TRepository repository)
        {
            _repository = repository;
        }

        [HttpGet]
        public virtual async Task<IEnumerable<IEntity>> Get()
        {
            return await _repository.GetAllRecords();
        }

    }
}
